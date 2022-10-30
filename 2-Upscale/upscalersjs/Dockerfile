FROM ubuntu:20.04

# Install NodeJS
RUN apt-get update
RUN apt-get install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_19.x | bash -
RUN apt-get install -y nodejs

# Install UpScalersJS
RUN npm install -g upscaler

RUN npm install log-timestamp
