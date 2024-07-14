#!/bin/bash

# Script para instalação de pacotes basicos no Arch Linux

# Atualizando o sistema
echo "Atualizando o sistema..."
sudo pacman -Syu

# Instalando pacotes

echo "Iniciando a instalação de pacotes..."

sudo pacman -S --needed \       # Instalação de pacotes necessários. Talvez adicionar o --noconfirm para instalação automática.
    git \                       # Sistema de controle de versão.
    vim \                       # Editor de texto.
    zsh \                       # Shell interativo.
    neofetch \                  # Ferramenta de informações do sistema.
    firefox \                   # Navegador web.
    flatpak \                   # Plataforma de distribuição de software.
    wget \                      # Ferramenta de download.
    curl \                      # Ferramenta de transferência de dados.
    htop \                      # Monitor de recursos.
    xorg \                      # Servidor gráfico.
    xorg-xinit \                # Inicializador do Xorg.
    bspwm \                     # Gerenciador de janelas.
    sxhkd \                     # Gerenciador de teclas.
    picom \                     # Compositor.
    rofi \                      # Lançador de aplicativos.
    nitrogen \                  # Configurador de plano de fundo.
    dunst \                     # Notificações.
    alacritty \                 # Emulador de terminal.
    flameshot \                 # Ferramenta de captura de tela com recursos de anotação.
    ranger \                    # Gerenciador de arquivos baseado em terminal.
    ntfs-3g \                   # Driver NTFS para montagem de partições NTFS.
    unzip \                     # Utilitário para descompactar arquivos.
    thunar \                    # Gerenciador de arquivos.
    thunar-volman \             # Gerenciador de dispositivos removíveis.
    thunar-archive-plugin \     # Plugin para arquivos compactados.
    fd \                        # Alternativa ao find.
    noto-fonts-emoji \          # Fonte com suporte a emojis.
    xdg-user-dirs \             # Cria diretórios padrões do usuário.
    vlc \                       # Reprodutor de mídia.
    brightnessctl \             # Controle de brilho.
    obsidian \                  # Aplicativo de anotações.
    openssh \                   # Conexão SSH.
    openssl \                   # Biblioteca de criptografia.

    # Bluetooth
    bluez \                    # Pilha de protocolos Bluetooth.
    bluez-utils \              # Utilitários para Bluetooth.

    # Audio
    pulseaudio \               # Servidor de som.
    alsa-utils \               # Utilitários ALSA.
    pulseaudio-alsa \          # Suporte a ALSA para PulseAudio.
    pulseaudio-bluetooth       # Suporte a Bluetooth para PulseAudio.
