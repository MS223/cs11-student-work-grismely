import random
my_randoms = random.sample(range(100), 15)
def find_odds(input):
    for x in input:
        if x % 2 == 1:
         print x

find_odds(my_randoms)

odd_list = []
def odd_sum(input):
    for x in input:
        if x % 2 == 1:
            odd_list.append(x)
    print sum(odd_list)
odd_sum(my_randoms)

even_list = []
def even_sum(input):
    for x in input:
        if x % 2 == 0:
            even_list.append(x)
    print sum(even_list)
even_sum(my_randoms)



