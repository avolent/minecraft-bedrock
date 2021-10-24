FROM debian
# Create the data volume for the container
VOLUME ["/data"]
WORKDIR /data
# Update and install required tools, clean up afterwards
RUN apt-get update && apt-get install -y unzip wget python && apt-get clean && rm -rf /var/lib/apt/lists/*
# Copy over build script file and change permissions
COPY ./build.py .
# Run build script
CMD ./build.py