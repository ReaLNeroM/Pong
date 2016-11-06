import Magic
import math
import Collisions

class Balls(object):
	def __init__(self, direction, radius):
		self.direction = direction
		self.y = Magic.Y / 2
		self.x = Magic.X / 2
		self.radius = radius

	def jump(self, steps, direction):
		self.y += steps * math.sin(direction)
		self.x += steps * math.cos(direction)

	def vertical_bounce(self):
		self.direction = - self.direction

	def horizontal_bounce(self):
		self.direction = math.pi - self.direction

	def move(self, steps, left_paddle, right_paddle):
		self.jump(steps, self.direction)

		if self.y - self.radius / 2 < 0:
			self.jump(-steps, self.direction)
			self.vertical_bounce()
		if self.y + self.radius / 2 > Magic.Y:
			self.jump(-steps, self.direction)
			self.vertical_bounce()
		if self.x - self.radius / 2 < 0:
			self.jump(-steps, self.direction)
			self.horizontal_bounce()
		if self.x + self.radius / 2 > Magic.X:
			self.jump(-steps, self.direction)
			self.horizontal_bounce()

		Collisions.collide(self, steps, left_paddle)
		Collisions.collide(self, steps, right_paddle)

		self.jump(steps, self.direction)
