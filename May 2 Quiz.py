# def max_value(number):
#     x = 0
#     while x < number:
#         print x
#         x = x + 1
#     print number
def max_value2(number):
  print range(1,number+1)
#prints values as a list
max_value(45)



def compare_list(list1,list2):
    if len(list1) == len(list2):
#only if list are of the same length or index
        for x in list1:
            if x > list2[list1.index(x)]:
                print x
            else:
                print list2[list1.index(x)]
#runs for element of mentioned index rather than index 

list3 = [5,6,7,8]
list4 = [3,6,7,7]
compare_list(list3,list4)


def swapping_stars():
    height = 6 #creates columns
    width = 3 #creates rows
    for x in range (0, height):
        if x % 2 == 1:
            print "- * " * width
        else:
            print '* - ' * width
swapping_stars()
