# ansible-nginx

Dockerfile

```
FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y openssh-server netcat net-tools curl wget && \
    apt-get clean all
# python and relevant tools 
RUN apt-get update && apt-get install -y \ 
        build-essential \ 
 python \ 
 python-dev \ 
 libxml2-dev \ 
 libxslt-dev \ 
 libssl-dev \ 
 zlib1g-dev \ 
 libyaml-dev \ 
 libffi-dev \ 
 python3-pip
# Latest versions of python tools via pip 
RUN pip install --upgrade pip \ 
 virtualenv \ 
 requests

EXPOSE 22 
CMD ["/usr/sbin/sshd", "-D"]
```

Build the image: 

```
docker build .
```

docker-compose.yml
```
version: '2'
services:
  fe1.dev:
    image: ubuntu
    hostname: fe1.dev
    ports:
      - "2224:22"
      - "8081:80"
     

  fe2.dev:
    image: ubuntu
    hostname: fe2.dev
    ports:
      - "2225:22"
      - "8082:80"
```

Run docker compose: 

```
docker-compose up -d
```

