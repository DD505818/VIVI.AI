
# Frontend Dockerfile
FROM node:16-alpine

WORKDIR /app

# Install dependencies
COPY package.json .
RUN npm install

# Copy app files
COPY . .

EXPOSE 3000

CMD ["npm", "start"]
