# -*- coding: utf-8 -*-

"""Quickly and easily add new monitored movies to your Radarr installation through Albert"""

from albertv0 import *
import json
import os
import requests
import configparser

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Radarr"
__version__ = "0.1"
__trigger__ = "radarr "
__author__ = "clearedTakeoff"
__dependencies__ = []

config = configparser.ConfigParser()
config.read("radarr.conf")
api_key = config["server"]["api"]
radarr_api = config["server"]["url"] + "/api/movie"
radarr_home = config["server"]["url"] + "/movies"

def handleQuery(query):
    if query.isTriggered:
        if len(query.string.strip()) >= 2:
            if query.string.strip() == "settings":
                return showSettings()
            else:
                return queryRadarrMovies(query.string.strip())
        else:
            return Item(
                        id=__prettyname__,
                        text="Search for a new movie",
                        subtext="Or use 'radarr settings' to display current configuration")


def showSettings():
    global config
    items = []
    items.append(Item(id="API Key", text="Current API key", subtext=config["server"]["api"]))
    items.append(Item(id="URL", text="Current server URL", subtext=config["server"]["url"]))
    return items

def queryRadarrMovies(query):
    global radarr_api
    global api_key
    global radarr_home
    response = requests.get(radarr_api + "/lookup?term=" + query + "&apikey=" + api_key)
    items = []
    for movie in response.json():
        movie_url = "https://themoviedb.org/movie/" + str(movie["tmdbId"])
        new_item = Item(id=movie["sortTitle"],
                        text=movie["title"] + " (" + str(movie["year"]) + ") " + str(movie["ratings"]["value"]),
                        subtext = movie["overview"],
                        actions = [FuncAction("Posting movie", lambda m=movie: postToRadarr(m))])
        items.append(new_item)
    return items

def postToRadarr(movie=None):
    global radarr_api
    global api_key
    #print("In here! Posting", movie)
    if movie is not None:
        movie["qualityProfileId"] = 0
        movie["profileId"] = 3
        movie["rootFolderPath"]= "/home/hd28/bytesaremine/media/Movies"
        movie["monitored"] = "true"
        movie["addOptions"]  = {"ignoreEpisodesWithFiles":"false","ignoreEpisodesWithoutFiles":"false","searchForMovie":"false"}
        headers = {"X-Api-Key": api_key}
        requests.post(radarr_api, headers=headers, data=json.dumps(movie))
