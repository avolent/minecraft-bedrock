#! /usr/bin/python
print("Downloading Minecraft Bedrock Server")
# Download - https://minecraft.azureedge.net/bin-linux/bedrock-server-1.17.40.06.zip
wget https://minecraft.azureedge.net/bin-linux/bedrock-server-1.17.40.06.zip

print("Unzipping and clean up")
unzip bedrock-server-1.17.40.06.zip && rm bedrock-server-1.17.40.06.zip

print("Starting Server")
./bedrock_server