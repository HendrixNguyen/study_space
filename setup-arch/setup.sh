#!/usr/bin/env bash
set -e


yay -Syu ibus-bamboo --noconfirm

if ! [ -z $(which docker)]; then
	yay -S docker docker-compose-cli --noconfirm
fi

if ! [ -z $(which ibus)]; then
	echo "export GTK_IM_MODULE=ibus" | tee -a /etc/profile
	echo "export QT_IM_MODULE=ibus"  | tee -a /etc/profile
	echo "export XMODIFIERS=@im=ibus"  | tee -a /etc/profile
  echo "export QT4_IM_MODULE=ibus"  | tee -a /etc/profile
	echo "export CLUTTER_IM_MODULE=ibus"  | tee -a /etc/profile
	echo "ibus-daemon -drx" | tee -a /etc/profile
fi

if [ -z $(which nvm) ]; then
	wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash
fi

if [ -z $(which k3d) ]; then
	wget -q -O - https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash
fi

if [ -z $(which kubectl) ]; then
	yay -Suy kubectl --noconfirm
fi
