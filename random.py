import random

chars = "abcdefghijklmnopqrstuvwxyz"
data = []

for i in range(50):
    data.append(random.choice(chars))

print(data)
