# FROM envoyproxy/envoy-alpine:v1.10.0
FROM python:3.7-alpine

COPY server/deploy/requirements.txt /tmp/requirements.txt
# COPY server/deploy/entrypoint.sh /tmp/entrypoint.sh

# RUN chmod +x /tmp/entrypoint.sh

RUN apk update & \
	apk add gcc libc-dev
RUN python3 -m pip install -r /tmp/requirements.txt

WORKDIR /app

# ENTRYPOINT tmp/entrypoint.sh

CMD python3 -u /app/index.py
 # & \
	# envoy -c /etc/service-envoy.yaml --service-cluster socket_server
