FROM archlinux:base-devel-20240101.0.204074

RUN pacman -Syu --noconfirm &&\\
    pacman -S --noconfirm git &&\\