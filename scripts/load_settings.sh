#!/bin/bash

# Configurando bspwm
echo "Configurando bspwm..."
mkdir -p $HOME/.config/{bspwm,sxhkd,polybar}
install -Dm755 $HOME/usr/share/doc/bspwm/examples/bspwmrc $HOME/.config/bspwm/bspwmrc
install -Dm644 $HOME/usr/share/doc/bspwm/examples/sxhkdrc $HOME/.config/sxhkd/sxhkdrc
install -Dm644 $HOME/usr/share/doc/polybar/config $HOME/.config/polybar/config
cp -r $HOME/etc/X11/xinit/xinitrc $HOME/.xinitrc

# # Configurando xdg-user-dirs
# echo "Configurando xdg-user-dirs..."
# xdg-user-dirs-update

# echo "Criando pastas no /.config..."
# mkdir -p $HOME/.config/{bspwm,sxhkd,polybar}
