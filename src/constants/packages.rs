pub const BASE_PACKAGES: &[&str] = &[
    "base",
    "base-devel",
    "sddm",
    "eza",
    "bat",
    "vim",
    "neovim",
    "kitty",
    "ntfs-3g",
    "git",
    "curl",
    "firefox",
    "htop",
    "neofetch",
    "zsh",
    "wget",
    "flatpak",
    // "superfile", Instalar via AUR
    "xdg-user-dirs",
    "zip",
    "unzip",
    "tar",
    "p7zip",
    "rustup",
    "openssh",
    "openssl",
    // "visual-studio-code-bin", Instalar via AUR
    "vlc",
    "fzf",
    "python",
    "qbittorrent",
    "nemo",
];

pub const NVIDIA_PACKAGES: &[&str] = &[
    "nvidia-settings",
    "nvidia-lts",
    "nvidia-utils",
    "opencl-nvidia",
    "linux-lts-headers",
    // "lib32-nvidia-utils",
];

pub const PIPEWIRE_PACKAGES: &[&str] = &[
    "pipewire",
    "pipewire-pulse",
    "pipewire-alsa",
    "pipewire-jack",
    "wireplumber",
];

pub const PULSEAUDIO_PACKAGES: &[&str] = &[
    "pulseaudio",
    "pulseaudio-alsa",
    "pulseaudio-jack",
    "pulseaudio-bluetooth",
    "pulseaudio-equalizer",
];

pub const BLUETOOTH_PACKAGES: &[&str] = &[
    "bluez",
    "bluez-utils",
    "bluez-plugins",
    "bluez-libs",
    "blueman",
];

pub const HYPERLAND_PACKAGES: &[&str] = &[
    "hyprland",
    "waybar",
    "dunst",
    "xdg-desktop-portal-hyprland",
    "qt5-wayland",
    "qt6-wayland",
    "hyprpaper",
    "hyprlock",
    "ttf-font-awesome",
    "ttf-firacode-nerd",
    "fuse2",
];

pub const QTILE_PACKAGES: &[&str] = &[
    "qtile",
    "picom",
    "dunst",
    "xdg-desktop-portal",
    "qt5-wayland",
    "qt6-wayland",
    "ttf-font-awesome",
    "ttf-firacode-nerd",
    "fuse2",
];