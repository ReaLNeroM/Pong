import pygame

def refresh_paddle(screen, paddle):
	pygame.draw.rect(screen, (0, 0, 0), paddle.area)
	pygame.draw.rect(screen, (255, 255, 255), paddle.draw())
	pygame.display.update(paddle.area)	

def remove_circle(screen, ball):
	pygame.draw.circle(screen, (0, 0, 0), (int(ball.x), int(ball.y)), ball.radius)
	pygame.draw.circle(screen, (255, 255, 255), (int(ball.x), int(ball.y)), 1)

def add_circle(screen, ball):
	pygame.draw.circle(screen, (255, 255, 255), (int(ball.x), int(ball.y)), ball.radius)
