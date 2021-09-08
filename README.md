# Infrastructure as Code 

Intro to what IaC is

## Ansible

How does Ansible fit into world of IaC

## How it Works

One control machine that has Ansible installed, Ansibe is not a requirement for the servers created. 

### Ansible Playbooks

YAML based 

## Installing Ansible 

[Instructions](https://docs.ansible.com/ansible/2.5/installation_guide/intro_installation.html#latest-releases-via-pip)

```
$ sudo easy_install pip
$ sudo pip install ansible
```

## Code-along

In this demo, we'll set up multiple front-end servers running Nginx using Docker containers. In case you aren't familiar, Nginx is a free, open-source and high-performance HTTP server that's popular for serving static websites. 

### Clone this repository 

Clone this repo and `cd` into it

### Set up SSH 

In order to be able to SSH into our containers we'll set up some SSH keys for this application. The following command will generate both the public (id_rsa.pub) and private part (id_rsa) of the key. 

```
$ ssh-keygen
```
**Note** When prompted to enter the filename enter `ansible_rsa` to avoid overwriting any SSH keys you might already have set up. You can also leave the passphrase empty also when prompted as this is only for demo purposes.

### Creating our Dockerfile 

A requirement of Ansible is Python, we'll also want to enable SSH as well to connect to our Docker containers. 

```Dockerfile
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
```
 



