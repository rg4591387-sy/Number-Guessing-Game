import random

target = (random.randint(1, 10))

while True:
    usserChoice = input("Guess the target or Quit :")
    if usserChoice == "Quit":
        break
    userChoice = int(usserChoice)
    if userChoice == target:
        print("success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number was  too small. Take a bigger guess..")
    else:
        print("your number was  too big. Take a smaller guess..")

print("-----Game Over-----")
