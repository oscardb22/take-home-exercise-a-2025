FROM node:22.15.1-bookworm-slim AS build

LABEL maintainer="Oscar Dominguez <oscardb22@gmail.com>"

WORKDIR /front_app

COPY front_test/package*.json ./

RUN npm install

COPY front_test/ .

EXPOSE 5173

CMD ["npm", "run", "dev", "--host 0.0.0.0"]
