#!/bin/sh

# Restaurar o fundo de tela com o Nitrogen (se já estiver em execução, mata e reinicia)
pidof -q nitrogen && killall nitrogen
pidof -q nitrogen || nitrogen --restore &

# Iniciar o Conky (se já estiver em execução, mata e reinicia)
pidof -q conky && killall conky
pidof -q conky || conky -c $HOME/.config/conky/qtile/dracula-01.conkyrc &

# Iniciar o xsettingsd (se já estiver em execução, mata e reinicia)
pidof -q xsettingsd && killall xsettingsd
pidof -q xsettingsd || xsettingsd --config="${HOME}/.config/qtile/configs/xsettingsd" >/dev/null 2>&1 &

# Iniciar o sxhkd (se já estiver em execução, mata e reinicia)
pidof -q sxhkd && killall sxhkd
pidof -q sxhkd || sxhkd -c $HOME/.config/qtile/configs/sxhkdrc &

# Iniciar o picom (se já estiver em execução, mata e reinicia)
pidof -q picom && killall picom
pidof -q picom || picom --config "${HOME}"/.config/qtile/configs/picom.conf &