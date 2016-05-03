
# consonants = []
# def de_vowel(some_string):
#     for x in some_string:
#         if x != "a" and x != "e" and x != "i" and x != "o" and x != "u":
# de_vowel("Hello")

vowels = ['a','e','i','o','u']
#list of vowels
def de_vowel(thing):
    for x in thing:
        if x in vowels:
            thing = thing.replace(x,"")
    print thing
#for every element in thing it will run through every element of the list vowels and if there is a match replace

de_vowel("Hello")
