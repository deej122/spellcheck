with open("/usr/share/dict/words") as dictionary:
    library = dictionary.read().lower().splitlines()
print library[100143], len(library)

"""
keeps /n

dictionary = open("/usr/share/dict/words")
library = dictionary.readlines()
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = ('aeiou')
word = input("> ").lower()
print word
'''
#set up trie data structure
class trieStruc:
	def __init__(self):
		self.word = None
		self.children = {}

		def insert(self,word):
			element = self
			for letter in word:
				if letter not in self.children:
					self.children[letter] = trieStruc()

				element = self.children[letter]

			element.word = word

#fill trie with words from dictionary			
trie = trieStruc()
for one in library:
	trie.insert(one)						

print trie
'''

#checks for duplicates and removes them and replaces all vowels with 'a'
def duplicates(w, v):
	import itertools
	import re
	#duplicates
	noDup = ''.join(ch for ch, _ in itertools.groupby(w))
	#vowels
	allNew = re.sub("[aeiou]", "a", noDup)
	return allNew


#binary search for words without any duplicates and vowels replaced with 'a'
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
        if library[midpoint] < newWord:
            lower = midpoint+1
        elif library[midpoint] > newWord:
            upper = midpoint-1
        else:
            found = True

    if found:
        print "Found it at", midpoint
    else:
		print "NO SUGGESTION"

#gets new word with no duplicates/replaced vowels
newWord = duplicates(word, "aeiou")

#searches for new word in dictionary + calculates Lev + provides suggestion
binarySearch()
print newWord
