#!/bin/sh   
read -p "avec ou sans touch ? " yn
    case $yn in
        avec ) xsetwacom set "Wacom Bamboo 16FG 4x5 Finger touch" Touch "on";;
        sans ) xsetwacom set "Wacom Bamboo 16FG 4x5 Finger touch" Touch "off";;
    esac
xsetwacom set "Wacom Bamboo 16FG 4x5 Pen stylus" rotate HALF
xsetwacom set "Wacom Bamboo 16FG 4x5 Pen eraser" rotate HALF
xsetwacom set "Wacom Bamboo 16FG 4x5 Finger touch" rotate HALF
xsetwacom set "Wacom Bamboo 16FG 4x5 Pad pad" button 3 key +ctrl z
xsetwacom set "Wacom Bamboo 16FG 4x5 Pad pad" button 8 key shift plus
xsetwacom set "Wacom Bamboo 16FG 4x5 Pad pad" button 9 key minus
xsetwacom set "Wacom Bamboo 16FG 4x5 Pad pad" button 1 key +ctrl +shift +a
