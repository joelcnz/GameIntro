import sys, pygame
from pygame.locals import *
from ball import *

def main():
	pygame.init()

	size = width, height = 320, 240
	black = 0, 0, 0

	screen = pygame.display.set_mode(size)

	# Initialise clock
	clock = pygame.time.Clock()
	
	character = Ball(width, height)
		
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: done = True

		character.move()
		
		screen.fill(black)
		character.draw(screen)
		pygame.display.flip()
		clock.tick(60)
	sys.exit()
if __name__ == '__main__': main()
