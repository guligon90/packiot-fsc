# Bioview Admin :: Servico local PostgreSQL
## Preliminares

Evidentemente, para que o dumping e restoring funcionem, é necessário que os serviços `cloudsqlproxyneopct` e `cloudsqlproxysysviz`,
já estejam rodando, pois é através desses serviços que o script de dump realiza a conexão com os bancos de dados.
Na mesma ordem de idéias, o serviço local de banco de dados, `devpgserver`, que contém os bancos de dados para
desenvolvimento, também deverá estar iniciado.

Na raiz do projeto, executar:
```bash
$ ./scripts/devenv.py build devpgserver | cloudsqlproxyneopct | cloudsqlproxyneopct # build da imagem
$ ./scripts/devenv.py start devpgserver | cloudsqlproxyneopct | cloudsqlproxyneopct # execução do contâiner
$ ./scripts/devenv.py logs devpgserver | cloudsqlproxyneopct | cloudsqlproxyneopct # logs do contâiner
```

## SQL Dumping:

Na raiz do projeto, executar:
```bash
$ ./scripts/devenv.py dump [db_user] [db_name] [db_password]
```

Espere o dump ser concluído. Se tudo ocorrer bem, na raíz do projeto, será criado um arquivo cujo nome tem o formato `{db_name}.dump`.
Esse arquivo será usado depois pelo script de restore.

## Restoring:

Com o dumping completo, executar no terminal:
```bash
$ ./scripts/devenv.py dump [db_name]
```

## Apontamentos no servidor de aplicação

Com os bancos de dados remotos restaurados localmente, é hora agora de fazer com que o contâiner do servidor de aplicação
consuma esses BDs. No [arquivo de variáveis de ambiente](../backend/docker/.neobiomeadmin.dev.env) do serviço `neobiomeadmin`,
por exemplo, assumindo um usuário e senha locais do PostgreSQL, os apontamentos para o DB do Neobiome Admin (proveninente do
servidor teste) ficariam como:

```bash
# Nomes dos BDs
NEOBIOME_ADMIN_DB_NAME=bioviewadmindb
NEOAPI_DB_NAME=neoapidb
SYSVIZ_DB_NAME=sysvizdb

# Credenciais unificadas (todos os BDs em um contâiner)
PGSQL_HOST=devpgserver
PGSQL_PORT=5433
PGSQL_USER=devuser
PGSQL_PASSWORD=devuser

# ...
```
## Navegação

* ["Raíz"](../../../README.md)
* ["Scripts"](../../../scripts/README.md)
* ["Cloud SQL proxies"](../cloudsqlproxy/README.md)
* ["Servidor de aplicação"](../../backend/README.md)
