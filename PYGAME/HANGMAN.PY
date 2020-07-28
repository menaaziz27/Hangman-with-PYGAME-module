import pygame
import os
import math
import random

#setup display
pygame.init()
WIDTH, HEIGHT = 900, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman Game')

#Font creation
Font = pygame.font.SysFont('comicsans' , 35)
word_font = pygame.font.SysFont('comicsans' , 60)
TITLE_FONT = pygame.font.SysFont('comicsans' , 70)

#Draw buttons of english alphapitical letters
#button variables
RADIUS = 20
GAP = 15
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65 #ASCI table
#Loop for calculating positions of all buttons
letters = []
for i in range(26):
	x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * ( i % 13))
	y = starty + ((i // 13) * (GAP + RADIUS * 2))
	letters.append([x, y, chr(A + i), True])
# print(letters)

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#extract all words from a file #####TODO
with open('sowpods.txt', 'r') as fr:
	words_list = []
	for line in fr:
		words_list.append(line.rstrip())
	# print(words_list)
#variables
hangman_word = random.choice(words_list).upper() #TODO
guessed = []

#load images
image_state = 0
images = []
for i in range(7):
	image = pygame.image.load('hangman' + str(i) + '.png')
	images.append(image)

# print(images)
FPS = 60
clockObj = pygame.time.Clock()
run = True

#display game statues (won / lost)
def display_message(message):
	pygame.time.delay(500)
	win.fill(WHITE)
	text = word_font.render(message, 1, BLACK)
	text2 = word_font.render('The word was '+ hangman_word , 1, BLACK)
	win.blit(text, (WIDTH/2 - text.get_width() / 2 , HEIGHT/2 - text.get_height()/2))
	win.blit(text2, (WIDTH/2 - text.get_width() - 100 / 2 , 300))
	pygame.display.update()
	pygame.time.delay(3000)

def draw():
	win.fill(WHITE)
	text = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
	win.blit(text, (WIDTH/2 - text.get_width()/2, 25))
	display_word = ''
	for letter in hangman_word:
		if letter in guessed:
			display_word += letter + ' '
		else:
			display_word += '_ '
	text = word_font.render(display_word, 1, BLACK)
	win.blit(text, (400,200))

	for letter in letters:
		x, y, ltr, visible = letter
		if visible:
			text = Font.render(ltr, 1, BLACK)
			win.blit(text, (x - text.get_width() / 2 , y - text.get_width() / 2 ))
			pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
	win.blit(images[image_state] , (150,100))
	pygame.display.update()


while run:

	clockObj.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			m_x, m_y = pygame.mouse.get_pos() #this function returns a tuple of x and y coordinate of mouse
			for letter in letters:
				x, y, ltr, visible = letter
				if visible:
					dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
					if dis < RADIUS:
						letter[3] = False
						guessed.append(ltr)
						if ltr not in hangman_word:
							image_state += 1

	draw()
	
	won = True
	for letter in hangman_word:
		if letter not in guessed:
			won = False
			break
	if won:
		# draw()
		display_message('You WON!')
		break

	if image_state == 6:
		# draw()
		display_message('You LOST!')
		break


pygame.quit()