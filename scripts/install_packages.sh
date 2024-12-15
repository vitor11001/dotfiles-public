#!/bin/bash

# Script para instalação de pacotes basicos no Arch Linux

# Atualizando o sistema
echo "Atualizando o sistema..."
sudo pacman -Syu

# Instalando pacotes

echo "Iniciando a instalação de pacotes..."

sudo pacman -S --needed --noconfirm \
    git \
    vim \
    zsh 
