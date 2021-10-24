#! /usr/bin/python
import os
#Global Variables
SERVER_NAME = "test"
GAMEMODE = ""
DIFFICULTY = ""
LEVEL_NAME = ""
ALLOW_CHEATS = ""
MAX_PLAYERS = ""
MAX_THREADS = "0"

print("Downloading Minecraft Bedrock Server")
# Download - https://minecraft.azureedge.net/bin-linux/bedrock-server-1.17.40.06.zip
os.system("wget https://minecraft.azureedge.net/bin-linux/bedrock-server-1.17.40.06.zip")

print("Unzipping and clean up")
os.system("unzip bedrock-server-1.17.40.06.zip && rm bedrock-server-1.17.40.06.zip")

print("Server Configuration")

print("Starting Server")
print(SERVER_NAME)
os.system("./bedrock_server")