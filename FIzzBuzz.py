def Fizzbuzz(whatever):
    for x in whatever:
        if x % 3 == 0 and x % 5 == 0:
#runs whatever numbers get plugged into the input divided by both numbers and compares the result to 0
            print "Fizzbuzz"
  #if it proves to be a multiple of both, prints phrase "fizzbuzz"
        elif x % 3 == 0:
#runs what numbers are plugged into the input divided by 3 and compares the result to 0
            print "Fizz"
  #if multiple prints phrase "fizz"
        elif x % 5 == 0:
#runs whatever number gets plugged into the input divided by 5 and compares the result to 0
            print "Buzz"
  #if it is a multiple it prints the phrase "buzz"
        else:
            print x
#if the number is not a multiple of 5 or 3 rather than one of the phrases it will be print the number

Fizzbuzz(range(1,101))
