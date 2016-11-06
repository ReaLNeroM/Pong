import Magic

class Paddles(object):

	def __init__(self, x_pos, sound):
		self.x = x_pos
		self.y = (Magic.Y - Magic.Paddle_Y) / 2
		self.area = (self.x, 0, Magic.Paddle_X, Magic.Y)

		self.last_moved = -Magic.Paddle_Delay

		self.sound = sound

	def incr(self, val):
		self.y -= val

		if self.y < 0:
			self.y = 0
		if self.y + Magic.Paddle_Y > Magic.Y:
			self.y = Magic.Y - Magic.Paddle_Y

	def draw(self):
		return (self.x, self.y, Magic.Paddle_X, Magic.Paddle_Y)