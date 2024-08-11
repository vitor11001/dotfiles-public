#!/bin/bash

echo "Atualizando o sistema..."
sudo pacman -Syu

# Instalando dependências
echo "Instalando pacotes necessários..."
sudo pacman -S --needed \
    xorg-server \       # O servidor X, necessário para qualquer ambiente gráfico.
    xorg-xinit \        # Inicializador do servidor X.
    xorg-xrandr \       # Utilitário para configurar a resolução da tela.
    xorg-xsetroot \     # Utilitário para definir a cor da raiz.
    xorg-xprop          # Utilitário para visualizar propriedades de janelas.

# Instalando bspwm
echo "Instalando bspwm e cia..."
sudo pacman -S --needed \
    bspwm \
    sxhkd 

# Instalando programas adicionais
echo "Instalando programas adicionais..."
sudo pacman -S --needed \
    kitty \
    firefox \
    rofi \
    vim \
    xdg-user-dirs-gtk \
    pavucontrol \
    openssh \
    thunar
