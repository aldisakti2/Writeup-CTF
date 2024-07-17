FROM oven/bun:latest

WORKDIR /app
COPY ./src .
RUN bun install

CMD [ "bun", "run", "app.js" ]
