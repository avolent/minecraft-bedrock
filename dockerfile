FROM debian
# Create the data volume for the container
ENV VERSION="1.17.40.06" \
    SERVER_NAME="Test" \ 
    GAMEMODE="survival" \
    DIFFICULTY="easy" \
    LEVEL_NAME="My World" \
    LEVEL_SEED="" \
    ALLOW_CHEATS="false" \
    MAX_PLAYERS="5" \
    MAX_THREADS="0"
# Add Data volume for docker
VOLUME ["/data"]
WORKDIR /data
# Update and install required tools, clean up afterwards
RUN apt-get update && \
    apt-get install -y unzip wget python && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
# Copy over build script file and change permissions
COPY ./build.py .
# Network Ports
EXPOSE 19132/udp
# Run build script
CMD ./build.py , ${VERSION}, ${SERVER_NAME}, ${GAMEMODE}, ${DIFFICULTY}, ${LEVEL_NAME}, ${LEVEL_SEED}, ${ALLOW_CHEATS}, ${MAX_PLAYERS}, ${MAX_THREADS}