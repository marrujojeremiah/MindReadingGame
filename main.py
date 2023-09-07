#importing a module that I need to be able to generate random numbers
import random

#I created a random even number between 2 and 10 by
#first randomizing an integer between 1 and 5. This will be
#final number. The number to add will take that and multiply it by 2.
randomFinalNumber = random.randrange(1, 5)
numberToAdd = randomFinalNumber * 2
#welcome message for game
print("Welcome to my mind reading game!\nYou may need a pencil and piece of paper handy.")
#Asking the user to enter in their name
name = input("Let's get started! What is your name?\n ")

#Prompts to walkthrough the game
print("Welcome " +name +", Let's see if I can read your mind.")
print("First, think of a number between 1 and 10.")
print("Multiply the result by 2.")
answer = input("Hit enter for the next step ")
print("Now, add...let's see...")
print(numberToAdd)
answer = input("Hit enter for the next step? ")
print("Now, divide the number you have by 2.")
answer = input("Hit enter for the next step? ")
print("Now, subtract the original number that you thought about.")
answer = input("Ready for the last step? Hit enter to continue.")

#Guessing the number
print("Well " +name +", let me read your mind...The number that you have right now is a....")
print(randomFinalNumber)

#In this block of code I am confirming the results. Showing the user how their number was correctly guessed
enteredNumber = int(input(">> To see the steps behind this: Enter in the number you originally picked between 1 and 10: "))
userNumber = enteredNumber * 2
print(">> Muliplied by 2 = " + str(userNumber))
userNumber = userNumber + numberToAdd
print(">> Told to add "+ str(numberToAdd) + " = " + str(userNumber))
userNumber = userNumber / 2
print(">> Divided by 2 = " + str(userNumber))
userNumber = userNumber - enteredNumber
print(">> Subtracted the original number "+ str(enteredNumber) +" = " + str(userNumber))
