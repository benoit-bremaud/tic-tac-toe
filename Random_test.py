import random

# Renvoie un élément aléatoire de la séquence non vide seq.
# Si seq est vide, lève IndexError

nbr = random.choice("123456789")
print(int(nbr))

nbr = random.choice("12345678")
print(int(nbr))

nbr = random.choice("1234567")
print(int(nbr))

nbr = random.choice("123456")
print(int(nbr))

nbr = random.choice("12345")
print(int(nbr))

nbr = random.choice("234")
print(int(nbr))

