#!/bin/sh

echo "Installing..."

SCRIPTPATH=$(pwd)
echo "We're here : ${SCRIPTPATH}"

echo "Installing resquests for sudo"
sudo -H pip install requests

echo "Making the wallpaper folder"
mkdir ~/Images/Wallpapers/Bing/

echo "Setting wallpaper"
gsettings set org.gnome.desktop.background picture-uri ~/Images/Wallpapers/Bing/current.jpg

echo "Putting script at startup"
sudo cp ${SCRIPTPATH}/get-wallpaper /etc/init.d/
sudo update-rc.d get-wallpaper defaults

echo "Starting..."
sudo service get-wallpaper start

exit 0
