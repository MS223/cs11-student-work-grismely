text_input = raw_input("Paste your text here").lower().split()
words = raw_input("What are you looking for?").lower()
dictionary = {}
dictionary['word count'] = text_input.count(words)
for x in text_input:
    dictionary[x] = dictionary.pop(x,0) + 1
print dictionary

#unnecessary 'word count' in the word count
#struggling
