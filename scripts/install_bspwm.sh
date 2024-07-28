#!/bin/bash

sudo pacman -S --needed \
    xorg \
    xorg-xinit \
    xclip \
    libxcb \
    xcb-utils-keysyms \
    xcb-util-cursor

# Instalando bspwm e sxhkd
sudo pacman -S --needed \
    bspwm \
    sxhkd \
    alacritty \
    rofi \
    polybar \
    vim \
    xdg-user-dirs-gtk \

mkdir -p $HOME/.config/{bspwm,sxhkd,polybar}
install -Dm755 /usr/share/doc/bspwm/examples/bspwmrc $HOME/.config/bspwm/bspwmrc
install -Dm644 /usr/share/doc/bspwm/examples/sxhkdrc $HOME/.config/sxhkd/sxhkdrc
install -Dm644 /usr/share/doc/polybar/config $HOME/.config/polybar/config
cp -r $HOME/etc/X11/xinit/xinitrc $HOME/.xinitrc
xdg-user-dirs-update
