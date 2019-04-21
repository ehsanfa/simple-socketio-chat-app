FROM python:3.7-alpine

COPY api-server/deploy/requirements.txt /tmp/requirements.txt

RUN python3 -m pip install -r /tmp/requirements.txt

WORKDIR /app

ENV FLASK_ENV=development
ENV FLASK_APP=index.py

CMD python -m flask run --host 0.0.0.0 --port 80
# CMD gunicorn -w 4 -b 0.0.0.0:80 index:app
