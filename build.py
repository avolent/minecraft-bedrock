#! /usr/bin/python
import os

print("Downloading Minecraft Bedrock Server")
# Download - https://minecraft.azureedge.net/bin-linux/bedrock-server-1.17.40.06.zip
os.system("wget https://minecraft.azureedge.net/bin-linux/bedrock-server-1.17.40.06.zip")

print("Unzipping and clean up")
os.system("unzip bedrock-server-1.17.40.06.zip && rm bedrock-server-1.17.40.06.zip")

print("Starting Server")
os.system("./bedrock_server")