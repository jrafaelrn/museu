FROM python:3

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y imagemagick ffmpeg

RUN sed -i '/<policy domain="path" rights="none" pattern="@\*"/d' /etc/ImageMagick-6/policy.xml

CMD [ "python", "main.py" ]
