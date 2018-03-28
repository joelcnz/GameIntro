import pygame

class Ball(pygame.sprite.Sprite):
	# Constructor
	def __init__(self, width, height):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		self.speed = [2, 2]
		self.width = width
		self.height = height
		self.ball = pygame.image.load("intro_ball.gif")
		self.ballrect = self.ball.get_rect()
		self.pos = [10,10]
		self.dir = [0,0]
		self.bounce = False
		self.hit = pygame.mixer.Sound('sfx\hit.wav')

	def setBounce(self, bounce):
		self.bounce = bounce
	
	def moveBounce(self):
		self.pos[0] += self.speed[0]
		self.pos[1] += self.speed[1]
		if self.pos[0] < 0 or self.pos[0] + self.ballrect.width > self.width:
			self.speed[0] = -self.speed[0]
			self.hit.play()
		if self.pos[1] < 0 or self.pos[1] + self.ballrect.height > self.height:
			self.speed[1] = -self.speed[1]
			self.hit.play()

	def userControl(self):
		self.pos[0] += self.dir[0]
		self.pos[1] += self.dir[1]

	def move(self):
		if self.bounce:
			self.moveBounce()
		if not self.bounce:
			self.userControl()

	def draw(self, screen):
		screen.blit(self.ball, self.pos)