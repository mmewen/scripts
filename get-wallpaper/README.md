get-wallpaper
=======

A small Python script to download the Bing picture everyday and set it as my Gnome Shell wallpaper

### Explanations

Well, it's pretty simple:
* It takes the HTML
* Finds the picture URL
* Downloads it in ~/Images/Wallpapers/Bing/
* Set it as wallpaper

### Setup

* Install `requests` for sudo : `sudo -H pip install requests`
* Edit the /path/to/this/repo/get-wallpaper.sh script to match your path
* Copy the script to the init.d dir : `sudo cp /path/to/this/repo/get-wallpaper /etc/init.d/get-wallpaper`
* Run `sudo update-rc.d get-wallpaper defaults`

### TO DO

* Think about making an INSTALL.sh
