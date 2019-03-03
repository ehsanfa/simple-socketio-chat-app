FROM nginx:alpine

COPY client/deploy/client.chat-app.dev /etc/nginx/conf.d/default.conf

COPY client/deploy/entrypoint.sh /tmp/entrypoint.sh

RUN chmod +x /tmp/entrypoint.sh

ENTRYPOINT /tmp/entrypoint.sh

WORKDIR /app