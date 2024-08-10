#!/bin/bash

# Instalando dependências
echo "Instalando pacotes necessários..."
sudo pacman -S --needed \
    xorg \
    xorg-xinit \
    xclip \
    libxcb \
    xcb-utils-keysyms \
    xcb-util-cursor

# Instalando bspwm
echo "Instalando bspwm e cia..."
sudo pacman -S --needed \
    bspwm \
    sxhkd \
    alacritty \
    rofi \
    polybar \
    vim \
    xdg-user-dirs-gtk \
