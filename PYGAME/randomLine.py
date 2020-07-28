import random

lines = open('sowpods.txt', 'r').read().splitlines()
print(random.choice(lines))
