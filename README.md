# Minecraft-bedrock Server in Docker
The following is a Minecraft-bedrock server in which i will be using in AWS ECS.

Start server with the following command
`docker run -it -p 19132:19132/udp minecraft-bedrock`

The following variables can be used to adjust server settings
eg.do `docker run -it -p 19132:19132/udp -e MAX_PLAYERS=1 -e SERVER_NAME="Dedicated" minecraft-bedrock`

VERSION="1.17.40.06"
SERVER_NAME="Test"
GAMEMODE="survival"
DIFFICULTY="easy"
LEVEL_NAME="My World"
LEVEL_SEED=""
ALLOW_CHEATS="false"
MAX_PLAYERS="5"
MAX_THREADS="0"