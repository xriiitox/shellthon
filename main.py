#!/usr/bin/env python3
import os
import socket

from run_command import run_cmd


def main():
    running = True

    while running:
        ps1: str = f"{os.getlogin()}@{socket.gethostname()}:{os.getcwd()} $"
        stuff = input(ps1 + " ")
        if stuff:
            run_cmd(stuff)


if __name__ == "__main__":
    main()
