#!/bin/bash

# Função para solicitar confirmação
confirm() {
    while true; do
        read -p "$1 [y/n]: " yn
        case $yn in
            [Yy]* ) return 0;;
            [Nn]* ) echo "Operação cancelada."; exit;;
            * ) echo "Por favor, responda com 'y' ou 'n'.";;
        esac
    done
}

# Verifica se o usuário tem privilégios de root
if [ "$EUID" -ne 0 ]; then
    echo "Por favor, execute como root (use sudo)."
    exit
fi

echo "Atualizando o sistema..."
confirm "Você deseja atualizar o sistema?"
sudo pacman -Syu

# Instalando dependências do Xorg
echo "Instalando pacotes necessários..."
confirm "Você deseja instalar os pacotes do Xorg?"
sudo pacman -S --needed \
    xorg-server \
    xorg-xinit \
    xorg-xrandr \
    xorg-xsetroot \
    xorg-xprop \
    xorg-xev

confirm "Você deseja instalar os drivers NVIDIA e ferramentas?"
sudo pacman -S --needed \
    nvidia \
    nvidia-utils \
    nvidia-settings \
    linux-headers

# Configurando o Xorg
confirm "Você deseja configurar o Xorg com o nvidia-xconfig?"
sudo nvidia-xconfig

# Instalando bspwm
echo "Instalando bspwm e cia..."
confirm "Você deseja instalar bspwm e sxhkd?"
sudo pacman -S --needed \
    bspwm \
    sxhkd 

# Instalando fontes
echo "Instalando fontes..."
confirm "Você deseja instalar as fontes necessárias?"
sudo pacman -S --needed \
    ttf-fira-code \
    ttf-font-awesome \
    noto-fonts-emoji \
    ttf-roboto

# Instalando outros pacotes essenciais
echo "Instalando pacotes necessarios..."
confirm "Você deseja instalar pacotes essenciais como bluetooth, pipewire, etc.?"
sudo pacman -S --needed \
    bluez \
    bluez-utils \
    blueman \
    htop \
    ntfs-3g \
    pipewire \
    pipewire-alsa \
    pipewire-pulse 

# Habilitando serviços
echo "Habilitando bluetooth..."
confirm "Você deseja habilitar o serviço bluetooth?"
sudo systemctl enable bluetooth

# Instalando programas adicionais
echo "Instalando programas adicionais..."
confirm "Você deseja instalar programas adicionais como kitty, firefox, etc.?"
sudo pacman -S --needed \
    kitty \
    firefox \
    rofi \
    vim \
    xdg-user-dirs-gtk \
    pavucontrol \
    openssh \
    thunar \
    nitrogen \
    curl \
    htop \
    picom \
    openssh \
    openssl \
    procps-ng

# Atualiza os diretórios padrão do usuário
xdg-user-dirs-update

# Instalando o paru
echo "Instalando o paru..."
confirm "Você deseja instalar o paru?"
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/paru.git
cd paru || exit 1  # Garante que o script pare se o diretório não for acessível
makepkg -si
cd ..
rm -rf paru  # Remove o diretório clonado do paru

# Instalando programas do AUR
echo "Instalando programas do AUR..."
confirm "Você deseja instalar o ttf-meslo-nerd-font-powerlevel10k?"
paru -S ttf-meslo-nerd-font-powerlevel10k

echo "Instalando sddm..."
confirm "Você deseja instalar e habilitar o sddm?"
sudo pacman -S --needed sddm
sudo systemctl enable sddm

# Cria o arquivo bspwm.desktop em /usr/share/xsessions
echo "Criando o arquivo bspwm.desktop..."
confirm "Você deseja criar o arquivo bspwm.desktop?"
cat <<EOF > /usr/share/xsessions/bspwm.desktop
[Desktop Entry]
Name=BSPWM
Comment=Binary Space Partitioning Window Manager
Exec=bspwm
Type=Application
EOF

echo "Arquivo bspwm.desktop criado com sucesso!"

# Configurando bspwm
echo "Configurando bspwm..."
confirm "Você deseja configurar o bspwm?"
mkdir -p $HOME/.config/{bspwm,sxhkd}
install -Dm755 /usr/share/doc/bspwm/examples/bspwmrc $HOME/.config/bspwm/bspwmrc
install -Dm644 /usr/share/doc/bspwm/examples/sxhkdrc $HOME/.config/sxhkd/sxhkdrc

echo "Instalação e configuração concluídas com sucesso!"
