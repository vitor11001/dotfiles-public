#!/bin/bash

# Será necessario instalar o python para o script
sudo pacman -S --needed --noconfirm \
    base-devel \
    python \
    pyenv \
    poetry

# Baixando a versão do python 3.12.7
pyenv install 3.12.7

# Definindo a versão do python 3.12 como global
pyenv global 3.12.7

# venv para o projeto
poetry install --no-root
