#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}Starting installation for ShadowDeauth-DF...${NC}"

OS=$(uname -s)

if [[ "$OS" == "Linux" ]]; then
    echo -e "${GREEN}Detected Linux environment.${NC}"
    if [ -x "$(command -v apt)" ]; then
        sudo apt update && sudo apt upgrade -y
        sudo apt install -y python3 python3-pip python3-venv aircrack-ng
    elif [ -x "$(command -v yum)" ]; then
        sudo yum update -y
        sudo yum install -y python3 python3-pip aircrack-ng
    else
        echo -e "${RED}Unsupported Linux package manager. Install Python3 and pip manually.${NC}"
        exit 1
    fi
    pip3 install --upgrade scapy rich pyfiglet

elif [[ "$OS" == "Darwin" ]]; then
    echo -e "${GREEN}Detected macOS environment.${NC}"
    if ! [ -x "$(command -v brew)" ]; then
        echo -e "${GREEN}Installing Homebrew...${NC}"
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    echo -e "${GREEN}Installing Python3 and pip...${NC}"
    brew install python3
    brew install aircrack-ng
    pip3 install --upgrade scapy rich pyfiglet

elif [[ "$OS" == "CYGWIN"* || "$OS" == "MINGW"* || "$OS" == "MSYS"* ]]; then
    echo -e "${GREEN}Detected Windows environment.${NC}"
    echo -e "${GREEN}Make sure you have Python3 installed from https://www.python.org/downloads/.${NC}"
    pip install --upgrade scapy rich pyfiglet
else
    echo -e "${RED}Unsupported operating system: $OS${NC}"
    exit 1
fi

if [[ "$EUID" -ne 0 ]]; then
    echo -e "${RED}Please run this installer as root or with sudo.${NC}"
    exit 1
fi

echo -e "${GREEN}Setting up the tool...${NC}"
chmod +x shadowdeauth-DF.py

echo -e "${GREEN}Installation completed successfully!${NC}"
echo -e "${GREEN}To run the tool, use the following command based on your system:${NC}"
echo -e "${GREEN}Linux/macOS: sudo python3 shadowdeauth-DF.py${NC}"
echo -e "${GREEN}Windows: python shadowdeauth-DF.py${NC}"
