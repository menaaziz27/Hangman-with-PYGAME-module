import random
import os

#TODO open the words file and pick random word


words = 'sowpods.txt'

lis = []
with open (words, 'r') as fr:
    for line in fr:
        lis.append(line.strip())
    random_word = random.choice(lis)

print(random_word)

def hangman():
    num_of_digits = '_ ' * len(random_word)
    print(num_of_digits)
    print("It's a " + str(len(random_word)) +" letters word")
    list_of_stripped_digits = num_of_digits.split()
    counter = 0
    number_of_guesses = 0 
    while True:
        inp = input("Enter you guess character :")
        if len(inp) == 1:
            if inp in random_word:
                number_of_guesses += 1
                indices = [ i for i,a in enumerate(random_word) if a == inp]
                for changeIndices in indices:
                    list_of_stripped_digits[changeIndices] = inp
                os.system("cls" if os.name == 'nt' else 'clear')
                print(" ".join(list_of_stripped_digits))
                newlyguessed = "".join(list_of_stripped_digits)
                if newlyguessed == random_word:
                    print("Congrats!! you won!\nYou have guessed the word in " + str(number_of_guesses) + " guesses!")
                    break
                else:
                    continue
            else:
                os.system("cls" if os.name == 'nt' else 'clear')
                print("Try again")
                counter += 1
                number_of_guesses += 1
                print("You have " + str(6 - counter) + ' tries!')
                if counter < 6:
                    print(" ".join(list_of_stripped_digits))
                    continue
                else:
                    print("Game over, you have tried 6 times\nThe word was " + random_word)
                    break
        else:
            number_of_guesses += 1
            print('invalid input, you should input only one character')

if __name__ == "__main__":
    hangman()    
