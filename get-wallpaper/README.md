get-wallpaper
=======

A small Python script to download the Bing picture everyday and set it as my Gnome Shell wallpaper

## Setup

* Install `pip` : `sudo apt install python-pip`
* Install `requests` for sudo : `sudo -H pip install requests`
* Edit the /path/to/this/repo/get-wallpaper/get-wallpaper script to match your path
* Copy the script to the init.d dir : `sudo cp /path/to/this/repo/get-wallpaper/get-wallpaper /etc/init.d/get-wallpaper`
* Run `sudo update-rc.d get-wallpaper defaults`
* Create the directory where the pictures will be downloaded : `mkdir ~/Images/Wallpaper && mkdir ~/Images/Wallpaper/Bing`
* Start the service : `sudo service get-wallpaper start`
* Run `gsettings set org.gnome.desktop.background picture-uri file:///home/mewen/Images/Wallpapers/Bing/current.jpg`

##

* Think about making an INSTALL.sh
