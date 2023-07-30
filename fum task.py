print("Hello\n")
print("Choose an Option :\n1) Start Game 1 Dice\n2) Exit")
choice = input("Enter a Choice: ")
import random

while True:
   if choice=="1":
      roll = random.randint(1,6)
      print("Dice Roll Result: " , roll)
      if roll==6:
         print("congratulation! you won a bonus roll")
         bonus_roll = random.randint(1,6)
         print("bonus roll result: " , bonus_roll)
      else:
         break
      
   if choice=="2":
      break
   else:
      print("invalid choise")
      
      

    