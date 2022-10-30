FROM node:16

WORKDIR /app
COPY . /app/

# Install dependencies
RUN npm install -g upscaler 
RUN npm install -g log-timestamp

CMD [ "node", "main.js" ]