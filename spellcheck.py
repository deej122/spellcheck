with open("/usr/share/dict/words") as dictionary:
    library = dictionary.read().lower().splitlines()
print library, len(library)

"""
keeps /n

dictionary = open("/usr/share/dict/words")
library = dictionary.readlines()
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'

word = input("> ").lower()
print word

def binarySearch():
    global found, lower, upper, midpoint
    lower = 0
    upper = len(library)-1
    found = False
    while lower <= upper and not found:
        midpoint = (lower + upper) / 2
        print "M: ", midpoint
        print "U: ", upper
        print "L: ", lower
        if library[midpoint] < word:
            lower = midpoint+1
        elif library[midpoint] > word:
            upper = midpoint-1
        else:
            found = True

    if found:
        print "The word is spelled correctly", midpoint
    else:
    	correct(word)

"""def correct(word):"""

binarySearch()
