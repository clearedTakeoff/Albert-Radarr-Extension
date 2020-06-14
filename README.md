# Radarr on Albert

This is a very basic extension to the Albert launcher on Linux, allowing you to add a new movie to the list of your monitored movies. It uses *radarr* as the trigger word.

## Installation

    git clone https://github.com/clearedTakeoff/Albert-Radarr-Extension.git ~/.local/share/albert/org.albert.extension.python/modules/Radarr
After cloning, edit *radarr.conf* to include URL to your Radarr server, API key and path to the movies folder on your system.
Copy *radarr.conf* to the Albert config folder: *$HOME/.config/albert/* and finally enable the extension within the Albert Python extensions.

## Usage

Use trigger word *radarr* and enter name of the movie you are looking for and select the correct result. This will send a POST request to your Radarr installation and add a new movie to the list.

You can use *radarr settings* to review your current configuration.
