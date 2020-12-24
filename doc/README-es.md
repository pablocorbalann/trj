<p align="center"><img alt="TRJ" src="../img/logo.png"></p>

<p align="center">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/pblcc/trj?color=5d3535&label=SIZE&style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/pblcc/trj?label=STARS&style=flat-square&color=5d3535">
  <img src="https://img.shields.io/github/watchers/pblcc/trj?color=5d3535&label=WATCHERS&style=flat-square">
  <img alt="GitHub forks" src="https://img.shields.io/github/forks/pblcc/trj?color=5d3535&label=FORKS&style=flat-square">
</p>


<p align = "center">
  <a href="README-es.md">Español</a> |
  <a href="../README.md">English</a>
</p>

## Tabla de contenido
- [Tabla de contenido](#tabla-de-contenido)
- [Idea](#idea)
- [Instalación](#instalación)
  - [Requisitos previos](#requisitos-previos)
  - [Compilación del cliente](#compilación-del-cliente)
  - [Ejecutando el servidor](#ejecutando-el-servidor)
- [Aviso legal](#aviso-legal)
  - [Licencia](#licencia)
  - [Garantía](#garantía)
  

<p align="center"><img src="../img/br.png"></p>

## Idea
Trc es un caballo de Troya creado con la intención de tener ** acceso completo al sistema informático de otra persona **, acceder a su cmd / terminal y poder ejecutar cualquier comando**.

Para lograr esto, se utiliza un servidor programado en Python que se conecta a un socket programado en C desde el lado del cliente.

<p align="center"><img src="../img/bl.png"></p>

## Instalación

Para usar Trj, tendrá que instalar dos cosas, el cliente y el servidor. El cliente ha sido programado usando C, ya que se puede compilar y el objetivo del ataque no notará que hay software espía ejecutándose como un hilo. El servidor está programado en Python.
### Requisitos previos

| Nombre | Uso | Enlaces |
| ------ | ----- | ------- |
| Git | Clonar del repositorio | [Instalar](https://git-scm.com/downloads) |
| Python (v3.6 +) | Ejecutar el servidor | [Página](https://python.org) |
| Compilador de C (gcc) | Compilar el cliente | [GNU](https://gcc.gnu.org/) |

El primer paso para instalar trj es clonar el repositorio en su máquina local:
```
git clone https://github.com/pblcc/trj
```

### Compilando el cliente
Para compilar el cliente usamos un compilador de C como [gcc](https://gcc.gnu.org) y [CMake](https://cmake.org). Ejecute los siguientes comandos:
```
cd client/
```
```
make
```
Ahora puede iniciar el cliente como:
```
./client
```

### Ejecutando el servidor
Para ejecutar el servidor, debe usar [Python](https://python.org). Ejecute los siguientes comandos:
```
python server/server.py
```
###### NOTA: Si tienes varias instalaciones de Python, usa Python3

<p align="center"><img src="../img/br.png"></p>

## Aviso legal
Trc se puede utilizar con fines maliciosos, por lo que tenemos que especificar un par de cosas.
### Licencia
Este proyecto está bajo la [Licencia](LICENCE)
### Garantía
Use tcr ** bajo su propio riesgo **, no soy responsable de ningún uso poco ético que haga con este repositorio. Este repositorio ha sido programado para uso educativo.**
