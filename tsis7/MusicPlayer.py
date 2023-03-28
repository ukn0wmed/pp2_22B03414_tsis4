import sys

import pygame
import os

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Music Player")

music_files = os.listdir("music")
current_track = 0

pygame.mixer.music.load("music/" + music_files[current_track])
pygame.mixer.music.play()

play_key = pygame.K_SPACE
stop_key = pygame.K_ESCAPE
next_key = pygame.K_RIGHT
prev_key = pygame.K_LEFT

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == play_key:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == stop_key:
                pygame.mixer.music.stop()
            elif event.key == next_key:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load("music/" + music_files[current_track])
                pygame.mixer.music.play()
            elif event.key == prev_key:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load("music/" + music_files[current_track])
                pygame.mixer.music.play()

    pygame.display.update()
