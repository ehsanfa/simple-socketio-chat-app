FROM python:3.7-alpine

COPY server/deploy/requirements.txt /tmp/requirements.txt

COPY server/deploy/entrypoint.sh /tmp/entrypoint.sh

RUN chmod +x /tmp/entrypoint.sh

RUN apk update & \
	apk add py3-pip py-virtualenv
RUN python3.7 -m pip install -r /tmp/requirements.txt

WORKDIR /app

# ENTRYPOINT tmp/entrypoint.sh

CMD python3.7 -u /app/index.py
