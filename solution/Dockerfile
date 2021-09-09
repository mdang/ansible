FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y openssh-server pwgen netcat net-tools curl wget && \
    apt-get clean all

RUN apt-get update && apt-get install -y \ 
        build-essential \ 
        python3 \ 
        python-dev \ 
        libxml2-dev \ 
        libxslt-dev \ 
        libssl-dev \ 
        zlib1g-dev \ 
        libyaml-dev \ 
        libffi-dev \ 
        python3-pip

RUN pip install --upgrade pip \ 
 virtualenv \
 requests

# Enable SSH access
RUN mkdir /var/run/sshd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN mkdir /root/.ssh
COPY ansible_rsa.pub /root/.ssh/authorized_keys
RUN chmod 400 /root/.ssh/authorized_keys

# Port 22 for SSH and 5000 for Flask
EXPOSE 22 5000
CMD ["/usr/sbin/sshd", "-D"]