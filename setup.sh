#!/bin/sh

echo "Setting up dotfiles..."
set -e                          # Exit em caso de erro.

# Especifique um diretório de configuração padrão se ele ainda não estiver definido.
XDG_CONFIG_HOME="${XDG_CONFIG_HOME:-$HOME/.config}"

