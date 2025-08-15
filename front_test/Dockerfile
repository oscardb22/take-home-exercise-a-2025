FROM node:22.15.1-bookworm-slim AS build

LABEL maintainer="Oscar Dominguez <oscardb22@gmail.com>"

WORKDIR /front_app

COPY front_test/package*.json ./

RUN npm install

COPY front_test/ .

# RUN npm run build

# FROM nginx:alpine

# COPY --from=build /front_app/dist /usr/share/nginx/html

EXPOSE 5173

# CMD ["nginx", "-g", "daemon off;"]
CMD ["npm", "run", "dev", "--host 0.0.0.0"]


# curl -X 'GET' 'http://backend:8000/api/parking/garage/' -H 'accept: application/json'