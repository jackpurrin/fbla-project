import time
import os

# Stands for In Game Time
igt = 0
hunger = 50
happiness = 50
money = 1000
sleeping = False

cat = """\
      \    //
       )  ( ')
      (  /  )
       \(__)|
"""

dog = """\
           __
      (___()'`;
      /,    /`
      //"--//

"""

os.system('cls' if os.name == 'nt' else 'clear')

print("Which do you want? A cat or a dog?")

pet = input()

if pet == "cat":
    print(cat)
elif pet == "dog":
    print(dog)
else: 
    print(seal)

