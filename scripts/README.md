# PackIOT :: Scripts for development enviroment (`devenv`)

De modo a facilitar a construção dos serviços declarados no `docker-compose.yml`, foi criado o script `devenv.py`, que
encapsula as ações relevantes a serem executadas tanto via `docker-compose` ou `docker`.

## Utilização

Para tornar o script `devenv` executável, basta rodar o seguinte comando:
```bash
$ chmod +x scripts/devenv.py
```

Finalmente, para conferir a documentaçãd de cada comando do `devenv`, você pode rodar:
```bash
$ ./scripts/devenv.py usage
```

## Navegação

* ["Root"](../README.md)
* ["PostgreSQL server"](../database/README.md) 
