#!/usr/bin/env bash

LOG_DIR=$PWD/log
DB_DIR=$PWD/db
ILOG=$LOG_DIR/install.log

mkdir -p $LOG_DIR $DB_DIR

status_check() {
    if [ $? -eq 0 ]
    then
        echo -e "$1 - Installed"
    else
        echo -e "$1 - Failed"
    fi
}

debian_install() {
    echo -e '=====================\nINSTALLING FOR DEBIAN\n=====================\n' > "$ILOG"

    echo -ne 'Python3\r'
    sudo apt -y install python3 python3-pip &>> "$ILOG"
    status_check Python3
    echo -e '\n--------------------\n' >> "$ILOG"

    echo -ne 'PIP\r'
    sudo apt -y install python3-pip &>> "$ILOG"
    status_check Pip
    echo -e '\n--------------------\n' >> "$ILOG"
}

termux_install() {
    echo -e '=====================\nINSTALLING FOR TERMUX\n' > "$ILOG"

    echo -ne 'Python3\r'
    apt -y install python &>> "$ILOG"
    status_check Python3
    echo -e '\n--------------------\n' >> "$ILOG"
}

arch_install() {
    echo -e '=========================\nINSTALLING FOR ARCH LINUX\n' > "$ILOG"

    echo -ne 'Python3\r'
    yes | sudo pacman -S python3 python-pip --needed &>> "$ILOG"
    status_check Python3
    echo -e '\n--------------------\n' >> "$ILOG"

    echo -ne 'PIP\r'
    yes | sudo pacman -S python-pip --needed &>> "$ILOG"
    status_check Pip
    echo -e '\n--------------------\n' >> "$ILOG"
}

echo -e '[LOG] Installing Dependencies...\n'

if [ -f '/etc/arch-release' ]; then
    arch_install
else
    if [ "$OSTYPE" == 'linux-android' ]; then
        termux_install
    else
    
        debian_install
    fi
fi

pip3 install -r requirements.txt &>> "$ILOG"

echo -e '=========\nCOMPLETED\n' >> "$ILOG"

echo -e '\n[<<] Log Saved:' "$ILOG"
