import pygame, sys
from pygame.locals import *

pygame.init()
lchsFont = pygame.font.Font("bauerg.ttf", 64) # Load Font
lchsFontSmall = pygame.font.Font("bauerg.ttf", 32) # Load Font
lchsLogo = pygame.image.load("lchs.png") # Load logo image
display = pygame.display.set_mode((800, 350)) # Create window
pygame.display.set_caption("LCHS Logo Redesigner (Press enter to switch between top and bottom text!)") # Set window title
text = "LCHS" # Default text
text2 = "LEDUC COMPOSITE" # Also default text
ct = 0 # What text to edit

while True:
	display.fill((255, 255, 255)) # Clear screen
	
	display.blit(lchsLogo, (400 - (lchsLogo.get_rect().width / 2), 10)) # Draw logo image
	t = lchsFont.render(text, True, (0, 0, 0)) # Render text
	display.blit(t, (400 - (t.get_rect().width / 2) - 10, 225)) # Draw text
	t2 = lchsFontSmall.render(text2, True, (209, 68, 52))
	display.blit(t2, (400 - (t2.get_rect().width / 2) - 10, 305))
 	
	for event in pygame.event.get(): # Handle events
		if(event.type == QUIT): # Quit event
			pygame.quit()
			sys.exit(0)
		elif(event.type == pygame.KEYDOWN): # Keyboard event
			if event.key == pygame.K_BACKSPACE:
				if ct == 0:
					text = text[:-1]
				else:
					text2 = text2[:-1]
			elif event.key == pygame.K_RETURN:
				if ct == 0:
					ct = 1
				else:
					ct = 0
			else:
				if ct == 0:
					text += event.unicode
				else:
					text2 += event.unicode
		
	pygame.display.update() # Update screen
