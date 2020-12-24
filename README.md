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
  
<p align="center"><img src="img/br.png"></p>

## Idea
Trc is a Trojan horse created with the intention of having **full access to someone else's computer system**, accessing their cmd/terminal and being able to execute any command. 

To achieve this, a server programmed in Python is used that connects to a socket programmed in C from the client side.
<p align="center"><img src="img/explication.png"></p>
<p align="center"><img src="img/bl.png"></p>

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
For compiling the client we use a C compiler as [gcc](https://gcc.gnu.org) and [CMake](https://cmake.org). Run the following commands:
```shell
cd client/
```
```shell
make
```
Now you can start the client as:
```
./client
```

### Running the server
To run the server you should use [Python](https://python.org). Run the following commands:
```shell
python server/server.py
```
###### NOTE: If you have multiple instalations of Python, use Python3

<p align="center">
  <img  src="img/banner.png">
</p>

 <p align="center"><img src="img/br.png"></p>

## Legal advice
Trc can be used for malicious purposes so we have to specify a couple of things.
### License
This project is under the BSL [License](LICENSE)
### Warranty
Use tcr **at your own risk**, I am not responsible for any unethical use you make with this repository. This repository has been programmed for educational use.
