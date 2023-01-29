## import he following libraries
import random
import time
##open the 8ball responses text file.
f = open('magic8ballresps.txt', 'r')
##read the file and store each line in a list
responses = f.readlines()
##Ask the user to input a Yes or No question
question = input("Please ask me a question.")
##paues for a couple secounds to emulate thinking :)
time.sleep(2)

print(random.choice(responses))