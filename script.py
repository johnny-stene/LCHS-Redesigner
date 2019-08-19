import pygame, sys
from pygame.locals import *

pygame.init()
lchsFont = pygame.font.Font("bauerg.ttf", 64) # Load Font
lchsLogo = pygame.image.load("lchs.png") # Load logo image
display = pygame.display.set_mode((800, 300)) # Create window
pygame.display.set_caption("LCHS Logo Redesigner") # Set window title
text = "LCHS" # Default text

while True:
	display.fill((255, 255, 255)) # Clear screen
	
	display.blit(lchsLogo, (400 - (lchsLogo.get_rect().width / 2), 10)) # Draw logo image
	t = lchsFont.render(text, True, (0, 0, 0)) # Render text
	display.blit(t, (400 - (t.get_rect().width / 2) - 10, 225)) # Draw text
 	
	for event in pygame.event.get(): # Handle events
		if(event.type == QUIT): # Quit event
			pygame.quit()
			sys.exit(0)
		elif(event.type == pygame.KEYDOWN): # Keyboard event
			if event.key == pygame.K_BACKSPACE:
				text = text[:-1]
			else:
				text += event.unicode
		
	pygame.display.update() # Update screen
