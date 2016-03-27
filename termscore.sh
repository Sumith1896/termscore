#!/bin/bash
ROOTUID="0"

if [ "$(id -u)" -ne "$ROOTUID" ] ; then
    echo "This script must be executed with root privileges."
    exit 1
fi

echo "Installing wt20 \m/\n"
pip install urllib2 2> /dev/null
pip install bs4 2> /dev/null
pip install prettytable 2> /dev/null
wget http://cse.iitb.ac.in/~sumith/wt20.py 2> /dev/null
mv ./wt20.py ~/
echo "alias wt20='watch python2 wt20.py'" >> ~/.bashrc
echo "\nSuccessfully installed!"
echo "Usage: \n$ wt20 <team1> <team2>"