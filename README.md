# Infrastructure as Code 

Intro to what IaC is

## Ansible

How does Ansible fit into world of IaC

## How it Works

One control machine that has Ansible installed, Ansibe is not a requirement for the servers created. 

### Ansible Playbooks

YAML based 

## Installing Ansible 

[!Instructions](https://docs.ansible.com/ansible/2.5/installation_guide/intro_installation.html#latest-releases-via-pip)

## Code-along

In this demo, we'll set up multiple front-end servers running Nginx using Docker containers. In case you aren't familiar, Nginx is a free, open-source and high-performance HTTP server that's popular for serving static websites. 

### Set up SSH 

In order to be able to SSH into our containers we'll set up some SSH keys for this application. The following command will generate both the public (id_rsa.pub) and private part (id_rsa) of the key. 

**Note** When prompted to enter the filename you can just hit enter. You can also leave the passphrase empty also when prompted as this is only for demo purposes.

```
$ mkdir webapp && cd webapp
$ ssh-keygen
```

 



