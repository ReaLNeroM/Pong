import pygame

def init():
	pygame.mixer.init()

_sound_library = {}

def play_music(path):
	init()
	pygame.mixer.music.load(path)
	pygame.mixer.music.play(-1)

def play_sound(paddle):
	song = pygame.mixer.Sound(paddle.sound)
	song.play()

