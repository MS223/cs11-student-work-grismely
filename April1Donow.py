# For each example below, predict what will be printed. Then, run the code and confirm your prediction.

a = 0
while a < 100:
	print a
"""
Prediction: The code is going to infinitely print "0" because it is equal to a and as long as a is less than a 100 it
will print a
Observation: infinitely print "0"
 """

a = 0
while a < 100:
	a = a + 1
	print a
"""
Prediction: Will print something like a count down except increasing rather than decreasing and will start at 1 rather
than 0 because the action to add one comes before printing a, will stop at 100
Observation:Counted up until 100

 """

a = raw_input("Would you like to quit: ")
while a != "y":
	a = raw_input("Would you like to quit: ")
"""
Prediction: Will print question and if a does not equal "y" it will print the question again
Observation: Prints question if a equals anything but "y" will infinitely print question
 """
