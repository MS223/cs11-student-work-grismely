my_dictionary = {
'cat': 'a domestic feline',
'dog': 'a domestic canine',
'chair': 'furniture piece for sitting',
'car': 'automobile'
}
print my_dictionary
print my_dictionary['dog']
print my_dictionary.get('dog')
print 'cat' in my_dictionary
print 'monkey' in my_dictionary
print my_dictionary['chair']
print my_dictionary['kittens']
#1. The entire "dictionary" prints as well as the value assigned to dog and finally true and false is printed
#2. my_dictionary is similar to a list, it can contain both strings and integers
#4. You recieve an error, this error means that in the data set dictionary there is no valued assigned under the name 'kittens',it does not exist in the set
