FROM python:3.6-alpine

RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories

RUN apk update && apk add chromium chromium-chromedriver

RUN pip install --upgrade pip
RUN pip install selenium

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /code

COPY code .

ENTRYPOINT [ "python",'app.py' ] 