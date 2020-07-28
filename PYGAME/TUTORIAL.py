import random, pygame, math

#window borders
WIDTH = 800
HEIGHT = 500

#initialize screen
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman clone')

#colors
blue = (153,204,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
grey = (160,160,160)

#Constant variables
FPS = 60
clock = pygame.time.Clock()
title_color = (34,196,179)
title = 'Hangman Game'

#Button variables
RADIUS = 20
GAP = 15
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65

#getting the center (x, y) position of each circle of all 26 button
letters = []
for i in range(26):
	x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * ( i % 13))
	y = starty + ((i // 13) * (GAP + RADIUS * 2))
	letters.append([x, y, chr(A + i), True])


#Font
font = pygame.font.SysFont('comicsans', 60)
alphabitcal_font = pygame.font.SysFont('comicsans', 30)
#words
words = open('sowpods.txt').read().splitlines()
Hangman_word = random.choice(words).upper()
guessed = []


#load images
image_state = 0
images = []
for i in range(7):
	image = pygame.image.load('hangman' + str(i) + '.png')
	images.append(image)


def draw():
	win.fill(grey)
	text = font.render(title, 1, BLACK)
	win.blit(text, (WIDTH/2 - text.get_width()/2, 25))
	display_word =''
	for letter in Hangman_word:
		if letter in guessed:
			display_word += letter +' '
		else:
			display_word += '_ '
	word = font.render(display_word, 1, WHITE)
	win.blit(word, (400,200))

	for letter in letters:
		x, y, ltr, visible = letter
		if visible:
			pygame.draw.circle(win, BLACK, (x,y), RADIUS, 2)
			text = alphabitcal_font.render(ltr, 1, BLACK)
			win.blit(text, (x - text.get_width()/2 , y - text.get_height()/2))
	# ren1 = font.render('hey',1, WHITE)
	# win.blit(ren1, (startx,starty - 200))
	win.blit(images[image_state], (100,120))
	pygame.display.update()


print(Hangman_word)
run = True
while run:

	clock.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			for letter in letters:
				x, y, ltr, visible = letter
				x_pos, y_pos = pygame.mouse.get_pos()
				dis = math.sqrt((x - x_pos)**2 + (y - y_pos)**2)
				if visible:
					if dis < RADIUS:
						letter[3] = False
						guessed.append(ltr)
						if ltr not in Hangman_word:
							image_state += 1
							if image_state > 6:
								run = False
			
	draw()


pygame.quit()