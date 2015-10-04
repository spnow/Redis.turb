#!/bin/bash

##
# requirement :
#     - Valgrind
#     - TcpDump
##
if ! (valgrind --version &> /dev/null); then
    echo "$(tput setaf 1)[Error] Please install: Valgrind"
    exit 1
fi

if ! (tcpdump --version &> /dev/null); then
    echo "$(tput setaf 1)[Error] Please install: TcpDump"
    exit 1
fi

echo "$(tput setaf 2)[+] go go go Valgrind:" $1

valgrind -q --trace-children=yes --xml=yes --xml-file=valgrind.xml --leak-check=full --leak-resolution=high $1 &

tcpdump 'port 6379'
