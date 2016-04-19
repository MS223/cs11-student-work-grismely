a = [1, 2, 4]
c = a
# Updating b will not affect a, because it did not directly change the list, now the variables are interchangeable.


# input: a list of ints
# output: an int
def update_list(a_list): #global, local
    a_list[3] = "yo" #local
    b = a_list[4] #local
    b = 100 #local
my_list = [1, 2, 3, 4, 5] #global
update_list(my_list)
print my_list
# The function will print out the list,my_list, and replace the value of index 3 with "yo"


var_1 = "kittens" #global
var_2 = "cookies" #global
# input: a string
# output: a string
def my_function(my_favorite_things): #global, local
    song_lyrics = "rain drops on roses," #local
    combined_song = song_lyrics + my_favorite_things #local
    return combined_song
# input: a string
# output: a string
def my_function_2(item, item2): #global, local
    full_lyrics = item + "on " + item2 #local
    full_song = my_function(full_lyrics) #local
    return full_song
my_song = my_function_2(var_1, var_2) #global


var_1 = 'cat' #global
var_2 = 'dog' #global

def print_out_my_favorite(favorite_pet): #global, local
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    if favorite_pet == var_2:
        print("My favorite pet is the dog.")

print_out_my_favorite(var_1)
print(var_2)


my_num = 2
def add2():
    return my_num + 1
def multiply_num(multiplier):
    return my_num * multiplier
def add2_and_multiply(multiplier):
    return add2()
    return multiply_num()

print add2_and_multiply(3)
