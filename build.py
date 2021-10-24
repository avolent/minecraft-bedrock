#! /usr/bin/python
import os
import sys
#Global Variables
argv = " ".join(sys.argv).split(", ")
SERVER_NAME = argv[1]
GAMEMODE = argv[2]
DIFFICULTY = argv[3]
LEVEL_NAME = argv[4]
ALLOW_CHEATS = argv[5]
MAX_PLAYERS = argv[6]
MAX_THREADS = argv[7]

print("\nDownloading Minecraft Bedrock Server")
# Download - https://minecraft.azureedge.net/bin-linux/bedrock-server-1.17.40.06.zip
os.system("wget https://minecraft.azureedge.net/bin-linux/bedrock-server-1.17.40.06.zip")

print("\nUnzipping and clean up")
os.system("unzip bedrock-server-1.17.40.06.zip && rm bedrock-server-1.17.40.06.zip")

print("\nSetting server config to the following")
print(argv)

print("\nStarting Server")

os.system("./bedrock_server")