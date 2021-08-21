#!/bin/bash

ENV_FILE=./scripts/sh/dev.env

if [ -f $ENV_FILE ]; then 
    echo "Arquivo existe"
    set -a
    . $ENV_FILE
    set +a
else
    echo "merda"
fi
