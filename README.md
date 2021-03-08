### ⚠️ Important note: I'm still developing trj. Let's try to get an alpha as soon as posible.

<p align="center"><img alt="TRJ" src="img/logo.png"></p>

<p align="center">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/pblcc/trj?color=5d3535&label=SIZE&style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/pblcc/trj?label=STARS&style=flat-square&color=5d3535">
  <img src="https://img.shields.io/github/watchers/pblcc/trj?color=5d3535&label=WATCHERS&style=flat-square">
  <img alt="GitHub forks" src="https://img.shields.io/github/forks/pblcc/trj?color=5d3535&label=FORKS&style=flat-square">
</p>

<p align="center">
  <a href="doc/README-es.md">Español</a>
</p>

## Table of contents
- [Table of contents](#table-of-contents)
- [Idea](#idea)
- [Installing](#installing)
  - [Prequisites](#prequisites)
  - [Compiling the Client](#compiling-the-client)
  - [Running the server](#running-the-server)
- [Legal advise](#legal-advice)
  - [License](#license)
  - [Warranty](#warranty)
- [Todo](#todo)
- [Advanced](#advanced)
  - [Modify the configuration of TRJ](#modify-the-configuration-of-trj)
  - [Modify the server IP and PORT using CLI](#modify-the-server-ip-and-port-using-cli)
  - [Compiling just the trojan code of trj](#compile-just-the-trojan-code)
  
<p align="center"><img src="img/br.png"></p>

## Idea
Trc is a Trojan horse created with the intention of having **full access to someone else's computer system**, accessing their cmd/terminal and being able to execute any command. 

To achieve this, a server programmed in Python is used that connects to a socket programmed in C from the client side.
<p align="center"><img src="img/bl.png"></p>

**THANKS TO ALL THE PERSONS THAT HAVE STARRED THE REPOSITORY!!!! LOVE YOU GUYS! ❤️**

<p align="center">
  <a href="https://github.com/pblcc/trj/stargazers">
    <img width="500px" src="https://reporoster.com/stars/pblcc/trj">
  </a>
</p>

## Installing

For using Trj, you will have to install two things, the client and the server. The client has been coded using C, as it can be compiled and the target of the attack will not notice that there is spyware running as a thread. The server is coded in Python. 
### Prequisites

| Name | Use | Links |
|------|-----|-------|
| Git  | Clonning the repository | [Install](https://git-scm.com/downloads) |
| Python (v3.6+) | Running the server | [Page](https://python.org) |
| C compiler (gcc) | Compiling the client | [Gnu](https://gcc.gnu.org/) |

The first step for installing trj is clonning the repository to your local machine:
```shell
git clone https://github.com/pblcc/trj
```

### Compiling the client
For compiling the client we use a C compiler as [gcc](https://gcc.gnu.org) and a Makefile. Run the following commands:
```shell
cd client/
```
```shell
make all
```
Now you move inside the directory using
```shell
cd build
```
And run the executable as:
```shell
./client.test
```
###### **NOTE**: Using make all you compile the complete client, if you just want to compile the trojan part of the code you can run make client, and if you want to compile the tests of trj use make test
```shell
make all # Compiles all the client
make client # Just compiles the actual code of the trj client
make test # Just compiles the tests of trj
```
### Running the server
To run the server you should use [Python](https://python.org). Run the following commands:
```shell
python server/server.py
```
###### NOTE: If you have multiple instalations of Python, use Python3
 <p align="center"><img src="img/br.png"></p>

## Legal advice
Trc can be used for malicious purposes so we have to specify a couple of things.
### License
This project is under the BSL [License](LICENSE)
### Warranty
Use tcr **at your own risk**, I am not responsible for any unethical use you make with this repository. This repository has been programmed for educational use.

## Todo
- ~Create a small server using in Python~
- ~Create a socket connection using C from the client to the server (tcp)~
- ~Implement this connection in a simple text chat~
- Upgrade the server so that it can manage more than one client at the same time
- ~Create the trojan in C inside `client/trojan`~
- ~Make the trojan run in a different thread~
- Include non-trojan code in a second thread, so that the user doesn't notice about the trojan
- **>** Export the configuration (yaml, json...)
- Add flags to the server (port, ip, execute, sudo...)
- Generate executables

## Advanced
### Modify the configuration of trj
To configurate the server and the client, check out the `configuration.yaml` file. There you have all the keys needed to configurate the complete server and the complete client. For example:

- The port of the server
- The IP adress
- The decodification format

And much more.

This configuration is loaded automatically.

If you want to check the configuration (in the server) you can use the `-c` flag.
```shell
cd server
python3 server.py -c
```

### Modify the server IP and port using CLI
You can modify the server IP and the server PORT from the console itself. Instead of running:
```shell
python server/server.py
```
Run:
```shell
python server/server.py <ip> <port>
```
For example:
```shell
python server/server 127.0.0.1 4404
```
### Compile just the trojan code
If you want just to compile the trojan code of the project, you can use:
```shell
git clone https://github.com/pblcc/trj
cd trj/client/trojan
make
```
After that you could run **just the trojan part of trj** using 
```shell
./trojan-code
```
