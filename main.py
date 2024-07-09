import os
import socket
import sys

import pygame
import pygame.freetype

from run_command import run_cmd

def main():
    ps1: str = f"{os.getlogin()}@{socket.gethostname()}:{os.getcwd()} $"
    path: str = os.getenv("PATH")
    
    running = True

    while running:
        ps1: str = f"{os.getlogin()}@{socket.gethostname()}:{os.getcwd()} $"
        stuff = input(ps1 + " ")
        if stuff:
            run_cmd(stuff)


if __name__ == "__main__":
    main()
