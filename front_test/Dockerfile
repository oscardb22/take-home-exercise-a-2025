# Stage 1: Build the application
# Use a Node.js base image for building the application
FROM node:22.15.1-alpine AS build

# Set the working directory inside the container
WORKDIR /front_test

# Copy package.json and package-lock.json
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of the application source code
COPY . .

# Build the React application for production using Vite
RUN npm run build

# Stage 2: Serve the application using a lightweight web server
# Use an NGINX base image for serving the static files
FROM nginx:alpine

# Copy the built application from the 'build' stage to the NGINX web root
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 to the host machine
EXPOSE 80

# Start NGINX and serve the application
CMD ["nginx", "-g", "daemon off;"]
