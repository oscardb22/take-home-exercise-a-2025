FROM node:22.15.1-bookworm-slim AS build

LABEL maintainer="Oscar Dominguez <oscardb22@gmail.com>"

WORKDIR /front_app

COPY front_test/ .
RUN apt-get update
RUN  apt-get install -y --no-install-recommends telnet
RUN npm install
RUN npm run build

FROM nginx:alpine

COPY --from=build /front_app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]


# curl -X 'GET' 'http://backend:8000/api/parking/garage/' -H 'accept: application/json'