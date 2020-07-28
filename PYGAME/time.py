import time 
import pygame

# pygame.init()
# clock = pygame.time.Clock()
# for i in range(10):
# 	clock.tick(1)

# print(int(round(pygame.time.get_ticks()/1000)))

pygame.init()
win = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
crashed = False
counter = 1 

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

	pygame.display.update()
	print(counter)
	counter += 1
	clock.tick(10) #we get 100 FPS in 10 second (10 frames per sec)
	# clock.tick(1) we get 10 fps in 10 seconds because it's 1 frame at sec
	#in other words make stop watch for 10 seconds with input(1 and another run with input 10)

	#summary this loop specify how the loop should be fast and how we want to display the screen speed