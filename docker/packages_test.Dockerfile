FROM archlinux:latest

RUN pacman -Syu --noconfirm \
 && pacman -S --noconfirm --needed sudo

# Adiciona um usuário não root para segurança durante o teste
RUN useradd -m tester && echo "tester ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Define o usuário padrão como o não root
USER tester

# WORKDIR /home/tester

# Copia o script para o contêiner
COPY ./target/debug/dotfiles-public ./dotfiles-public

RUN sudo chmod +x ./dotfiles-public

# RUN ./dotfiles-public

# CMD ["bash", "-c", "./base.sh | tee /home/tester/install_log.txt"]
# CMD ["tail", "-f", "/dev/null"]
# CMD ["bash", "-c", "./base.sh && tail -f /dev/null"]
CMD ["bash", "-c", "./dotfiles-public"]