import os
import socket
import sys

import pygame
import pygame.freetype

from run_command import run_cmd

def main():
    ps1: str = f"{os.getlogin()}@{socket.gethostname()}:{os.getcwd()} $"
    path: str = os.getenv("PATH")
    inp: str = f"{ps1} "
    currentLine = 0
    oldStdout = sys.stdout

    pygame.init()
    size = width, height = 1280, 720
    running = True

    screen = pygame.display.set_mode(size)
    font = pygame.freetype.Font("./RobotoMono.ttf", 16)

    while running:
        screen.fill((0, 0, 0))
        font.render_to(screen, (0,currentLine), inp, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(inp) > 0 and len(inp) != len(ps1)+1:
                        inp = inp[:-1]
                elif event.key != pygame.K_RETURN or event.key == pygame.K_TAB:
                    inp += event.unicode
                elif event.key == pygame.K_RETURN:
                    run_cmd(inp[:(len(ps1)+1)])
                    if oldStdout != sys.stdout:
                        currentLine += 1
                        font.render_to(screen, (0,currentLine), sys.stdout, (255, 255, 255))
        pygame.display.flip()


if __name__ == "__main__":
    main()
