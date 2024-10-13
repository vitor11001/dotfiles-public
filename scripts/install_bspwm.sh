#!/bin/bash

# Verifica se o usuário tem privilégios de root
if [ "$EUID" -ne 0 ]
  then echo "Por favor, execute como root (use sudo)."
  exit
fi

echo "Atualizando o sistema..."
sudo pacman -Syu

# Instalando dependências do Xorg
echo "Instalando pacotes necessários..."
sudo pacman -S --needed \
    xorg-server \       # O servidor X, necessário para qualquer ambiente gráfico.
    xorg-xinit \        # Inicializador do servidor X.
    xorg-xrandr \       # Utilitário para configurar a resolução da tela.
    xorg-xsetroot \     # Utilitário para definir a cor da raiz.
    xorg-xprop \        # Utilitário para visualizar propriedades de janelas.
    xorg-xev            # Utilitário para visualizar eventos do teclado e mouse.

sudo pacman -S --needed \
    nvidia \
    nvidia-utils \
    nvidia-settings \
    linux-headers

# Configurando o Xorg
sudo nvidia-xconfig

# Instalando bspwm
echo "Instalando bspwm e cia..."
sudo pacman -S --needed \
    bspwm \
    sxhkd 

# Instalando fontes
echo "Instalando fontes..."
sudo pacman -S --needed \
    ttf-firacode \
    ttf-font-awesome \
    noto-fonts-emoji \
    ttf-roboto

# Instalando outros pacotes essenciais
echo "Instalando pacotes necessarios..."
sudo pacman -S --needed \
    bluez \
    bluez-utils \
    blueman \
    htop \
    ntfs-3g \        # Driver NTFS
    pipewire \
    pipewire-alsa \
    pipewire-pulse \
    pipewire-bluetooth

# Habilitando serviços
echo "Habilitando bluetooth..."
sudo systemctl enable bluetooth

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
    thunar \
    nitrogen \
    curl \
    htop \
    picom \
    dunst \
    openssh \
    openssl \
    procps-ng

# Atualiza os diretórios padrão do usuário
xdg-user-dirs-update

# Instalando o paru
echo "Instalando o paru..."
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/paru.git
cd paru || exit 1  # Garante que o script pare se o diretório não for acessível
makepkg -si
cd ..
rm -rf paru  # Remove o diretório clonado do paru

# Instalando programas do AUR
echo "Instalando programas do AUR..."
echo "Instalando ttf-meslo-nerd-font-powerlevel10k..."
paru -S ttf-meslo-nerd-font-powerlevel10k

echo "Instalando sddm..."
sudo pacman -S --needed sddm
sudo systemctl enable sddm

# Cria o arquivo bspwm.desktop em /usr/share/xsessions
echo "Criando o arquivo bspwm.desktop..."

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
mkdir -p $HOME/.config/{bspwm,sxhkd}
install -Dm755 /usr/share/doc/bspwm/examples/bspwmrc $HOME/.config/bspwm/bspwmrc
install -Dm644 /usr/share/doc/bspwm/examples/sxhkdrc $HOME/.config/sxhkd/sxhkdrc
