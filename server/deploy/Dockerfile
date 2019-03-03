FROM envoyproxy/envoy-alpine

COPY server/deploy/requirements.txt /tmp/requirements.txt
COPY server/deploy/entrypoint.sh /tmp/entrypoint.sh
COPY server/deploy/service-envoy.yaml /etc/service-envoy.yaml

RUN chmod +x /tmp/entrypoint.sh

RUN apk update & \
	apk add python3 py3-pip
RUN python3 -m pip install -r /tmp/requirements.txt

WORKDIR /app

# ENTRYPOINT tmp/entrypoint.sh

CMD python3 -u /app/index.py & \
	envoy -c /etc/service-envoy.yaml --service-cluster socket_server
