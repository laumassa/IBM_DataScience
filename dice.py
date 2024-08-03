# TEST FILE FOR PYTHON & TERMINAL OUTPUT

from random import randint

def dice():
   result = randint(1,6)
   return result

value = dice()
print("Résultat du dé :", str(value))