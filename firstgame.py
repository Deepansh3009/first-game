import random

print("Welcome to the game in which you have to guess a number")
print()
print("what level do you want to play at: easy,medium,hard,impossible")
print()
print("easy:7 tries medium:5 tries hard:3 tries impossible:1 try")

level = input("Enter your level=").lower()

while level not in ["easy","medium","hard","impossible"] :
    print("Invalid level. Please choose easy, medium, hard, or impossible.")
    print()
    level = input("Enter your level=").lower()

if level=="easy":
    tries=7
elif level=="medium":
    tries=5
elif level=="hard":
        tries=3
elif level=="impossible":
      tries=1

print("I am thinking of a number")
print()

number=random.randint(1,100)
print("I have a number in my head,time for you to guess")
print()
print("you have", tries, "tries")

while tries>0 :
    guess=int(input("Enter your guess="))
    if guess < number:
        tries = tries - 1
        if tries == 0:
                    print("you have exhausted your tries, the number was", number)
                    break
        print("your guess is low, try again")
        print()
        print("you have", tries, "tries left")
    elif guess > number:
        tries = tries - 1
        if tries == 0:
                    print("you have exhausted your tries, the number was", number)
                    break
        print("your guess is high, try again")
        print()
        print("you have", tries, "tries left")
    else:
        print("congratulation, you have successfully guessed the number")
        break