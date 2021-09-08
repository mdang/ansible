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

## Setting up Docker

In this demo, we'll set up multiple front-end servers running Nginx using Docker containers. In case you aren't familiar, Nginx is a free, open-source and high-performance HTTP server that's popular for serving static websites. 

### Clone this repository 

Clone this repo and `cd` into it

### Enable SSH access

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
 
Build our Docker image and tag it as `ubuntu-ansible` for use later 
```
$ docker build . -t ubuntu-ansible
```

### Creating docker-compose.yml file 

We will use the `ubuntu-ansible` image as the base for our front-end web servers. We'll create two servers in this example but it could easily be expaded to include many more. 

```Dockerfile
version: '2'
services:
  fe1.dev:
    image: ubuntu-ansible
    hostname: fe1.dev
    ports:
      - "2224:22"
      - "8081:80"
  fe2.dev:
    image: ubuntu-ansible
    hostname: fe2.dev
    ports:
      - "2225:22"
      - "8082:80"
```

Now let's start our Docker containers: 

```
$ docker-compose up -d
```
[SCREENSHOT TERMINAL WITH TWO SERVERS UP]

If you open Docker Desktop, you should see the following two containers running. 

[SCREENSHOT DOCKER DESKTOP]

## Setting up Ansible

### Inventory file

TBD what is it used for 

```inventory
[fe-servers]
fe1.dev
fe2.dev
```

### ssh.config

If not present, Ansible will use the globah ssh configuration on your machine. 

```
Host *
    #disable host key checking: avoid asking for the keyprint authenticity
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null
    #enable hashing known_host file
    HashKnownHosts yes
    #IdentityFile allows to specify exactly which private key I wish to use for authentification
    IdentityFile ./ansible_rsa

Host fe1.dev
    HostName localhost
    User root
    Port 2224
Host fe2.dev
    HostName localhost
    User root
    Port 2225
```


