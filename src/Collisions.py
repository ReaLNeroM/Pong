import Sound
import Magic

def collide(ball, steps, paddle):
	reflect = ball.direction
	backwards = False

	for i in range(paddle.y, paddle.y + Magic.Paddle_Y + 1):
		if abs(i - int(ball.y)) ** 2 + abs(paddle.x - int(ball.x)) ** 2 < (ball.radius / 2) ** 2:
			backwards = True
			ball.horizontal_bounce()
		elif abs(i - int(ball.y)) ** 2 + abs(paddle.x + Magic.Paddle_X - int(ball.x)) ** 2 < (ball.radius / 2) ** 2:
			backwards = True
			ball.horizontal_bounce()
		if backwards:
			break

	for j in range(paddle.x, paddle.x + Magic.Paddle_X - 2):
		if abs(paddle.y - int(ball.y)) ** 2 + abs(j - int(ball.x)) ** 2 < (ball.radius / 2) ** 2:
			backwards = True
			ball.vertical_bounce()
		elif abs(paddle.y + Magic.Paddle_Y - int(ball.y)) ** 2 + abs(j - int(ball.x)) ** 2 < (ball.radius / 2) ** 2:
			backwards = True
			ball.vertical_bounce()
		if backwards:
			break

	if backwards:
		Sound.play_sound(paddle)
		ball.jump(steps, ball.direction)
