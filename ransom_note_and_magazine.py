#!/usr/bin/python

# find whether a ransom note can be formed from a given magazine

def unify_word(word):
	word = word.replace(",","")
	word = word.replace(",","")
	return word.lower()
	
	
def is_formed(notes, magazine):
	#split and preprocess
	sample = notes.split(" ")
	source_tmp = magazine.split(" ")
	source=set()
	
	for word in source_tmp:
		word = unify_word(word)
		source.add(word)
	
	for word in sample:
		word = unify_word(word)
		if word not in source:
			return False
	
	return True

print is_formed("These are a test","This is another test, that is not a correct one, just kidding")
		
		