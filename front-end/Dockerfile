# install dependencies
FROM node:18.8.0-alpine AS deps

WORKDIR /app
COPY ./package.json ./yarn.lock ./

RUN yarn install --frozen-lockfile

# build node project
FROM node:alpine AS builder
WORKDIR /app

COPY . .
COPY --from=deps /app/node_modules ./node_modules

ARG API_URL="https://djermy.com"
ENV REACT_APP_API_URL=$API_URL

RUN yarn build --production

# copy all web files and use nginx to serve
FROM nginx:1.23.3-alpine AS runner

WORKDIR /app

COPY --from=builder /app/build /usr/share/nginx/html/
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
