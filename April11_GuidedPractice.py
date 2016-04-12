# what does this function return ?
#The function will multiple the input by 2 and then print it
def print_only(x):
   y = x * 2
   print y

# how is this one different ?
#This function will be returning it rather than printing it meaning that the abswer will not be visualized
def return_only(x):
   y = x * 2
   return y #unlike the function before this one, the user will not be able to see the result because its return rather than print

# let's try to use our 2 functions
print "running print_only ..."
print_only(7) #the input value

print "running return_only ..."
return_only(7) #the input value

print "printing print_only ..."
print print_only(7)

print "printing return_only ..."
print return_only(7)

print "using print_only ..."
print_only(7) + 6

print "using return_only ..."
return_only(7) + 6
