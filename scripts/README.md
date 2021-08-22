# PackIOT FSC :: Development environment automation

<!-- TOC -->
## 0. Table of contents

- [1. Introduction](#1-introduction)
- [2. Getting started](#2-getting-started)
- [3. Where to now?](#3-where-to-now)
    
<!-- /TOC -->

## 1. Introduction
As mentioned before, in order to facilitate the building and running of the services listed in the `docker-compose.yml`, the `devenv.py`, was implemented.
This module automates the varios actions that can be performed via Docker Compos

```bash
scripts/
├── devenv.py       # The executable module
├── docker          # The library containing the helper scripts
│   ├── build.py
│   ├── clean.py
│   ├── common.py
│   ├── ...
└── README.md       # This very file
```

## 2. Getting started

To make the `devenv.py` module executable, just run the following command at the terminal:
```bash
$ chmod +x scripts/devenv.py
```

Finally, to check out the documentation of each script, you can run:
```bash
$ ./scripts/devenv.py usage
```

## 3. Where to now?

* [Database](../database/README.md) 
* [Root](../README.md)
* [Table of contents](#0-table-of-contents)
