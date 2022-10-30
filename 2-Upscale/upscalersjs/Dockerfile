FROM node:16

# Install dependencies
RUN npm install -g upscaler 
RUN npm install log-timestamp

WORKDIR /app
COPY . /app/

CMD [ "node", "main.js" ]