import sys, pygame
from pygame.locals import *
from ball import *
from base import *

def main():
	pygame.init()
	pygame.display.set_caption('Game Intro')

	size = width, height = 320, 240

	screen = pygame.display.set_mode(size)

	# Initialise clock
	clock = pygame.time.Clock()
	
	character = Ball(width, height)
	character.setBounce(True)

	# Display some text
	font = pygame.font.Font(None, 36)
	text = font.render("Press [Space]", 1, (0, 0, 0))
	textpos = text.get_rect()

	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: done = True
			
			if character.bounce == False:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP: character.dir[1] = -character.speed[1]
					if event.key == pygame.K_DOWN: character.dir[1] = character.speed[1]
					if event.key == pygame.K_LEFT: character.dir[0] = -character.speed[0]
					if event.key == pygame.K_RIGHT: character.dir[0] = character.speed[0]

				if event.type == KEYUP:
					if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						character.dir[1] = 0
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						character.dir[0] = 0

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					text = font.render("Space Pressed", 1, (0, 0, 0))

		character.move()
		
		screen.fill(GREEN)
		character.draw(screen)
		screen.blit(text, textpos)

		pygame.display.flip()
		clock.tick(60)
	sys.exit()
if __name__ == '__main__': main()