FROM buildpack-deps:bionic-scm AS builder

WORKDIR /tmp

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    g++ gcc libc6-dev make pkg-config
RUN apt-get install -y libssl-dev

RUN wget -q https://curl.se/download/curl-8.1.2.tar.gz && \
    tar xzf curl-8.1.2.tar.gz

WORKDIR /tmp/curl-8.1.2

RUN ./configure --prefix=/build \
    --disable-shared --enable-static --with-openssl \
    --disable-dict --disable-file --disable-ftps --disable-gopher \
    --disable-imap --disable-imaps --disable-ldap \
    --disable-ldaps --disable-pop3 --disable-pop3s --disable-rtmp --disable-rtsp \
    --disable-scp --disable-sftp --disable-smb --disable-smbs --disable-smtp \
    --disable-smtps --disable-telnet --disable-tftp && \
    make && \
    make install

FROM ubuntu:latest

EXPOSE 8080

RUN apt-get update
RUN apt-get install -y socat
RUN apt-get install -y figlet

COPY --from=builder /build/bin/curl /usr/sbin/curl
COPY --from=builder /usr/lib /usr/lib
COPY --chmod=755 ./app.sh /app/app.sh

WORKDIR /app
RUN useradd -ms /bin/bash ctf
USER ctf

CMD socat TCP-LISTEN:8080,fork EXEC:/app/app.sh,pty,stderr
