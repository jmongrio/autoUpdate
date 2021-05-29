#! /usr/bin/python3

import os

os.system("echo Updating...")
os.system("sudo apt-get update")
os.system("echo Upgrading...")
os.system("sudo apt-get upgrade")
os.system("echo Removing trash...")
os.system("sudo apt-get autoremove")