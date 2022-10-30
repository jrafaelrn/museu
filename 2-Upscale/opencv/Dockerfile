FROM ubuntu:20.04

# Install minimal prerequisites (Ubuntu 18.04 as reference)
RUN apt update && apt install -y cmake g++ wget unzip

# Download and unpack sources
RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
RUN wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.x.zip
RUN unzip opencv.zip
RUN unzip opencv_contrib.zip

# Create build directory and switch into it
RUN mkdir -p build && cd build

# Configure
RUN cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.x/modules ../opencv-4.x

# Build
RUN cmake --build .
RUN cd /usr/local
RUN make install

# Install Python
RUN apt install -y python3 python3-pip
RUN pip3 install opencv-python

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y


COPY . ./app
WORKDIR /app
ENTRYPOINT [ "python3", "main.py" ]