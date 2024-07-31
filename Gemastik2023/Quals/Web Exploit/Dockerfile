FROM debian:buster-slim

RUN apt update && apt install -y --no-install-recommends default-jre

COPY src/flag.txt /redacted

WORKDIR /opt/webtool
COPY src/webtool.jar .
COPY src/application.properties .

USER nobody

WORKDIR /opt/user_data
RUN mkdir template && \
    cp /usr/bin/md5sum /opt/user_data/template/md5sum && \
    cp /usr/bin/base64 /opt/user_data/template/base64

WORKDIR /opt/webtool
ENTRYPOINT ["java", "-Xmx256m", "-jar", "webtool.jar"]
