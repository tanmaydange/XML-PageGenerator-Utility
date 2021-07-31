FROM amazonlinux:latest
RUN yum install -y pip
RUN pip install supervisor
COPY . /app/
WORKDIR /app/
ENTRYPOINT ["supervisord","-n", "-c", "/app/supervisord.conf"]
