# Basic Commands:
01. docker version [Show the Docker version information]
02. docker ps [List containers]
03. docker images [List images]
04. docker build [Build an image from a Dockerfile]
05. docker create/ run [Create a new container/ Create+Run]
06. docker info [Display system-wide information]
07. docker stats [Display a live stream of container(s) resource usage statistics]
08. docker start/stop/kill [To enable or disable containers]
09. docker search [Search the Docker Hub for images]
10. docker pull/push [Pull or Push images with a docker registry]
11. docker login/logout [In or Out with a docker registry]
12. docker exec [Run a command in a running container]
13. docker config/container/image/network/swarm/system/volume [Management Commands]
14. docker inspect [Return low-level information on Docker objects/images/networks such as Ports, Metadata, etc.,]
15. docker pull learnitguide/busapp:latest [<user-name/image-name:tag>]


### Prerequisites:
- Windows 11 64-bit: Home or Pro version 21H2 or higher.
- Enable the WSL 2 feature on Windows. [wsl --install](https://learn.microsoft.com/en-us/windows/wsl/install)
- Enable Virtualization.
- Goto Turn Windows features on or off, then enable WSL and Hypervisor platform.

## Definitions:
- Container - Its a way of packaging the applications with all dependencies and configuration.
    - A portable artifact easily share and run in any environment.
    - Makes development and deployment more easy and efficient.
    - It has layers of images. Images can only readable. Containers has R/W access.
    - Disadvantage: has OS compatibility issue.
- Docker Registry - Where the images are stored.
- Virtualization - uses virtual machine with the help of 'iso' files. Has dedicated OS.
- Containerization - uses containers with the help of 'image' files. Has a single host OS.
- docker.io = DockerHub = Build + Ship + Run


## Commands Implementation:
```bash
- man docker-system-df [Another way to run commands but used for manual commands]
- docker volume ls
- docker volume help
- docker image help
- docker info
- docker swarm [Clustering environment like EKS]
- docker system help
- docker system df [Disk usage]
- docker system prune [Removes unused containers and images]
- docker search httpd, busapp, alpine, tomcat, python, mongodb [Check in DockerHub]
- docker pull httpd
```

## To run container:
```bash
- docker ps -a [List all exited, stopped and running containers]
- docker run --name web3 httpd (incorrect) [Create and Run a container with image name]
- docker run -d --name web3 httpd [To daemonize/detach the container to run in background]
```

## To login in container:
```bash
- docker exec -it web3 /bin/sh [To login in running container. -it(interactive terminal)]
    - # bash
    - root@b7e2fba112a6:/usr/local/apache2# cd /bin
    - root@b7e2fba112a6:/usr/local/apache2# ls -lrt[Longlisting Recursive Time]
    - root@b7e2fba112a6:/usr/local/apache2# cd /sbin
    - root@b7e2fba112a6:/usr/local/apache2# ls
    - root@b7e2fba112a6:/usr/local/apache2# uname -a
    Press Ctrl+D to exit from running container.
- docker exec web3 uname -a
- docker exec web3 mkdir /tmp/naren
- docker exec web3 ls /tmp
```

## Copy and Logs:
```bash
- docker cp <srcpath> container-name:<despath>
    - docker cp C:\Users\Naren\iNeuron\Screenshots\JSON.png web3:/tmp/
    - docker exec web3 ls /tmp/
- docker rm -f web3 [To remove container with forcifully]
- docker logs web3
```

## Using -it(interactive terminal) with bash for OS:
```bash
- docker run -d --name dummy alpine [Since alpine is not an application it will be exited]
- docker run -d -it --name dummy2 alpine /bin/bash [For os we need to use '-it' with 'bash']
- docker stats dummy2
- docker system prune
- docker pull ubuntu:latest
```

## Inspecting host and port:
```bash
- docker run -d --name myapp -p 81:80 httpd [custom-port:exposed-port]
- ipconfig /all (ip a = Linux) [ipconfig in Windows and ipv4 address]
- http://192.168.1.5:81/
- docker inspect <image-name:tag> or <image-id>
- docker run -d --name learnapp -p 8000:8001 learnitguide/busapp
- docker history learnitguide/busapp <image-name>
```

## Image save and load:
```bash
- docker save alpine:latest > alpine-bkp.tar
- docker load -i alpine-bkp.tar
- docker images -a -q
- docker rmi $(docker images -a -q)  [To use this command, you need to remove all containers]
```

## To modify image and commit:
```bash
- docker run -d -it --name myapp ubuntu /bin/sh
- docker exec -it myapp /bin/sh
- sudo apt-get update/ install curl [We can modify image inside running container]
- docker commit <container-name> <image-name:tag>
- docker login [To push image in private registry]
- docker tag <image-name:tag> naren10/<image-name:tag>
- docker push naren10/<image-name:tag>
```

## To build an image and run:
```bash
- docker build .
- docker build -f <dockerfile path>
- docker build -t myweb:latest .
- docker run -d -it --name myapp -p 80:80 myweb:latest
- docker run -d -it --name myapp -p 81:80 myweb:latest ping google.com [Results error when CMD as instruction]
```

#### CMD vs ENTRYPOINT:
- CMD = It can overrides the command in the container, if we add arguments at the end of container creation.
- ENTRYPOINT = It will never overrides the command in the container.

## Network commands:
```bash
- Network = Bridge(Docker0-172.17.0.1), None, Host
- docker network ls
- docker network create <network-name>
- docker network inspect <network-name>
```

## Simple_Flask_App: [host="0.0.0.0" | Port# in app.py and Dockerfile should be same]
```bash
- docker build -t flaskapp:latest .
- docker run -d --name myapp -p 5000:8000 flaskapp:latest
- docker tag flaskapp:latest naren10/flaskapp:latest
- docker push naren10/flaskapp:latest  [Pushed in docker.io]
```

## To Check usage and remove unwanted objects:
```bash
- docker system df
- docker system df -v [verbose]
- docker system prune
- docker system prune -a
```
