# Infrastructure as Code 

Intro to what IaC is

## Ansible

How does Ansible fit into world of IaC

## How it Works

### Ansible Playbooks

## Code-along

In this demo, we'll set up multiple front-end servers running Nginx using Docker containers. In case you aren't familiar, Nginx is a free, open-source and high-performance HTTP server that's popular for serving static websites. 

### Set up SSH 

In order to be able to SSH into our containers we'll set up some SSH keys for this application. The following command will generate both the public (id_rsa.pub) and private part (id_rsa) of the key. 

```
$ mkdir webapp && cd webapp
$ ssh-keygen
```

**Note** You can leave the passphrase empty when prompted as this is only for demo purposes. 



