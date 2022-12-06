# derbynames microservice

[![Docker](https://github.com/bdunnette/derbynames-zappa/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/bdunnette/derbynames-zappa/actions/workflows/docker-publish.yml)

Generating amusing (?) derby names using aitextgen.

## Building

```bash
docker build -t derbynames .
docker run -p 5000:5000 derbynames
```
