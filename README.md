# PackIOT FSC :: Challenge #1 [WiP]

Technical assessment for the position of full-stack software developer at PackIOT.


<!-- TOC -->
## 0. Table of contents

- [1. Preliminaries](#1-preliminaries)
    - [1.1. Installing pip and virtualenv](#11-installing-pip-and-virtualenv)
    - [1.2. Virtual environment](#12-virtual-environment)
- [2. Building and running](#2-building-and-running)
    - [2.1. PostgreSQL server](#21-postgresql-server)
        - [2.1.1 For building](#211-for-building)
        - [2.1.2 For running](#212-for-running)
    - [2.2. pgAdmin 4](#22-pgadmin-4)
- [3. Where to now?](#3-where-to-now)
<!-- /TOC -->

## 1. Preliminaries

In order to build the project, you must have already installed and configured in your workspace:


* [Docker](https://docs.docker.com/engine/install/ubuntu/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Python (3.8)](https://www.python.org/downloads/release/python-3810/)
* [pip](https://pip.pypa.io/en/stable/installation/)
* [virtalenv](https://virtualenv.pypa.io/en/latest/) (or any other suitable virtual environment manager for Python)

### 1.1. Installing pip and virtualenv

With the correct Python distribution, at the terminal, execute the following commands:
```bash
$ sudo apt install python3-pip python3-virtualenv
```
### 1.2. Virtual environment

After you cloned this project, you must install its Python dependencies. So, at the project's root, execute in the terminal:
```bash
$ virtualenv --python=python3 venv                  # Creates the virtual env
$ source venv/bin/activate                          # Make it active inside the project
$ pip install --upgrade pip --no-cache-dir          # Upgrade the package manager
$ pip install -r requirements.txt --no-cache-dir    # Install dependencies listed in the .txt file
```

## 2. Building and running

To construct the containers which encapsulate the [PostgreSQL](https://www.postgresql.org/) database server and the 
[pgAdmin 4](https://www.pgadmin.org/download/) web application, a suite of scripts was implemented in Python, in order
to automate the users' interaction with the Docker and Compose actions. The documentation about these scripts can be found [here](./scripts/README.md).

The aforementioned containers and its associated images are built with Docker Compose, where the corresponding services are all declared
in the [YAML file](./docker-compose.yaml), at the project's root. These services are:

* `pgsqlserver`: Runs the container that encapsulates a proper PostgreSQL server. The image for this container (`Dockerfile`) was implemented locally, for reasons of database automation;
* `pgadmin`: The web interface that consumes the PostgreSQL database, and for that it can not run without the previous service been built. It uses an officially distributed image, downloaded from [Docker Hub](https://hub.docker.com/r/dpage/pgadmin4/).

### 2.1. PostgreSQL server

We use here the automation script to perform building and runnning. At the project's root, execute in the terminal:
#### 2.1.1. For building: 
```bash
$ ./scripts/devenv.py build pgsqlserver 

```
#### 2.1.2. For running: 
```bash
$ ./scripts/devenv.py startwlogs pgsqlserver # Starts the container in detached mode and shows the logs
```

**Note**: The database for this challenge (`packiotfscdb`) is created when the container is started (you can see in the logs). To run the DDL statements and the queries implemented for this challenge, see [this documentation](./database/README.md).

### 2.2. pgAdmin 4

Similarly, we use the automation script to build and run this service, with the difference that the building part is not done separatedly, because the image for this container is obtained externally, i.e., there is no `Dockerfile`. So, you just need to run in the terminal:
```bash
$ ./scripts/devenv.py startwlogs pgadmin
```

## 3. Where to now?

* [Database](./database/README.md) 
* [Scripts](./scripts/README.md) 
* [Table of contents](#0-table-of-contents)
