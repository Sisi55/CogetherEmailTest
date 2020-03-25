FROM python:3.7-alpine

RUN apk update && \
    apk add python3 python3-dev \
            gcc musl-dev linux-headers zlib zlib-dev \
            freetype freetype-dev jpeg jpeg-dev libffi-dev \
            postgresql-dev curl nginx

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
ADD exampleapp.conf /etc/nginx/conf.d/exampleapp.conf

###
WORKDIR /etc/periodic
ADD crontab ./everymin/crontab
# 실행 권한 부여
RUN chmod a+x /etc/periodic/everymin/crontab
RUN dos2unix /etc/periodic/everymin/crontab

WORKDIR /etc/crontabs
RUN echo "*       *       *       *       *       run-parts /etc/periodic/everymin" >> root
###

# Cron 실행
RUN /usr/sbin/crond -f

ENV PYTHONUNBUFFERED 1
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 80