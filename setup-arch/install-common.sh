#!/usr/bin/env bash
set -e

function run_as_root() {
  if [ $(id -un) == root ]; then
    ${@}
  else
    sudo -sE ${@}
  fi
}

if [ -z $(which yay) ]; then
  run_as_root pacman -S --needed base-devel
  cd /opt
  run_as_root git clone https://aur.archlinux.org/yay-git.git
  run_as_root chown -R $(whoami):$(whoami) ./yay-git
  cd yay-git
  makepkg -si
fi

  yay -Syu --noconfirm

if [ -z $(which wget) ]; then
  yay -Su wget --noconfirm
fi

if [ -z $(which curl) ]; then
  yay -Su curl --noconfirm
fi

if [ -z $(which tar) ]; then
  yay -Su tar --noconfirm
fi

if [ -z $(which ping) ]; then
  sudo apt-get -qq install -y iputils-ping
fi

if [ -z $(which ip) ] || [ -z $(which route) ]; then
  yay -Su iproute2 --noconfirm
fi

if [ -z $(which netstat) ]; then
  yay -Su net-tools --noconfirm
fi

if [ -z $(which jq) ]; then
  yay -Su jq --noconfirm
fi

if [ -z $(which micro) ]; then
  curl -fsSL https://getmic.ro/ | bash
  sudo mv micro /usr/local/bin
fi