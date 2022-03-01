FROM node:17.5.0-bullseye

WORKDIR /ygo_marketplace/frontend
COPY package.json package-lock.json ./
RUN npm install

COPY webpack.config.js babel.config.json ./

CMD ["npm", "run", "dev"]

