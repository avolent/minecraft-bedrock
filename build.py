#! /usr/bin/python
import os
import sys
#Global Variables
argv = " ".join(sys.argv).split(", ")
VERSION = argv[1]
properties = {
    "server-name": argv[2],
    "gamemode": argv[3],
    "difficulty": argv[4],
    "level-name": argv[5],
    "level-seed": argv[6],
    "allow-cheats": argv[7],
    "max-players": argv[8],
    "max-threads": argv[9],
    }

print("\nDownloading Minecraft Bedrock Server")
# Download - https://minecraft.azureedge.net/bin-linux/bedrock-server-1.17.40.06.zip
os.system("wget https://minecraft.azureedge.net/bin-linux/bedrock-server-" + VERSION + ".zip")

print("\nUnzipping and clean up")
os.system("unzip bedrock-server-" + VERSION + ".zip" "&& rm bedrock-server-" + VERSION + ".zip")

print("\nSetting server config to the following")
for key, value in properties.items():
    os.system("sed -i 's/" + key + "=.*/" + key + "=" + value + "/' server.properties")

print("\nStarting Server")
os.system("./bedrock_server")