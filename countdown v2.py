# number = input("Number?")
# for x in range(1,number + 1):
#     print number
#     number = number - 1
# print "Boom!"
x = int(input("number?"))
while x > 0:
#condition, want ocuntdown to stop before 0 therefore as long as x is not 0 code will run
    print x
#if you dont print x you will not start with the number given to you by the user
    x = x - 1
#a countdown is a nubmber deducted by 1, this does that
print "boom!"
