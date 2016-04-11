import random

def mystery_function(x, y):
    random_number = random.randint(0,2) # What's the range of randoms?
    if random_number > 0: # What's the probability that random_number is greater than 0?
        z = x + y
    else:
        z = x * y
    print z
mystery_function(1, 2)

# What's the range of randoms?
'''The range of randoms is 0 and 1 because range is not inclusive.'''
#What's the probability that random_number is greater than 0?
'''The probablity that random_number is greater than 0 is 50% because you only have one another number besides 0.'''
#What happens when your run this code? How do you know what the result was?
'''When you run this code depending on whether the random number is larger than 0 the inputs will be added or multiplied by one another
I knew what the result would be because there is a condition that must be met and things that will happen
as a result of it being met or not'''
# Keeping the function the same, rewrite the code to print out the value that the function returns
