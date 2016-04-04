name = raw_input("What's your name?").capitalize()
print "Hello " + name
maxnum = input("Whats the largest number you'd like to guess from?")
userAnswer = input("Choose a number between 1 and " + str(maxnum) + "?")

import random
answer = random.randint(1,maxnum)

while userAnswer != answer:
    if userAnswer > answer:
        print "too high!"
    elif userAnswer < answer:
        print "too low!"

    userAnswer = input("Guess again?")
print answer
#tell user if theyre correct or not
