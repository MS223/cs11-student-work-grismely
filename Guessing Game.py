tries = 1
name = raw_input("What's your name?").capitalize()
print "Hello " + name
maxnum = input("Whats the largest number you'd like to guess from?")
userAnswer = input("Choose a number between 1 and " + str(maxnum) + "?")

import random
answer = random.randint(1,maxnum)

while userAnswer != answer:
    if userAnswer > answer:
        print "too high " + name + "!"
        tries = tries + 1
    elif userAnswer < answer:
        print "too low " + name + "!"
        tries = tries + 1
    userAnswer = input("Guess again?")
    if userAnswer == answer:
        print "You got it right!!"
print str(answer) + " is the answer!"
print "It took you " + str(tries) + " tries!"
