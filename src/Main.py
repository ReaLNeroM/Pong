import sys
import pygame
import Magic
import Draw
import random
import math
import Sound

pygame.init()
screen = pygame.display.set_mode((Magic.X, Magic.Y))

from Paddles import Paddles
from Balls import Balls

left_paddle = Paddles(Magic.Left_Paddle_X, Magic.Left_Sound)
right_paddle = Paddles(Magic.Right_Paddle_X, Magic.Right_Sound)

ball = Balls(random.random() * 2 * math.pi - math.pi, Magic.Ball_Size)

Draw.refresh_paddle(screen, left_paddle)
Draw.refresh_paddle(screen, right_paddle)

clock = pygame.time.Clock()

Sound.play_music(Magic.Music_Path)

frame = 0
while True:
	clock.tick(Magic.FPS)

	board = pygame.key.get_pressed()

	mouse = pygame.mouse.get_pos()

	left_paddle_speed = Magic.Paddle_Move
	if board[pygame.K_RSHIFT]:
		left_paddle_speed *= 3

	if board[pygame.K_UP]:
		left_paddle.incr(left_paddle_speed)
	if board[pygame.K_DOWN]:
		left_paddle.incr(-left_paddle_speed)

	left_paddle.incr(left_paddle.y - mouse[1] + Magic.Paddle_Y / 2)

	right_paddle_speed = Magic.Paddle_Move
	if board[pygame.K_LSHIFT]:
		right_paddle_speed *= 3

	if board[pygame.K_w]:
		right_paddle.incr(right_paddle_speed)
	if board[pygame.K_s]:
		right_paddle.incr(-right_paddle_speed)


	Draw.remove_circle(screen, ball)
	ball.move(Magic.Ball_Step, left_paddle, right_paddle)

	update_list = []

	update_list.append(Draw.refresh_paddle(screen, left_paddle))
	update_list.append(Draw.refresh_paddle(screen, right_paddle))
	Draw.add_circle(screen, ball)

	update_list.append((ball.x - 50, ball.y - 50, 100, 100))
	pygame.display.update(update_list)

	# event printing
	for event in pygame.event.get():
		#print (event.type)
		if event.type == 12:
			sys.exit()

	frame += 1







