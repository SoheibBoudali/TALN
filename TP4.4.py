words = ['attribution', 'confabulation', 'elocution', 'sequoia','tenacious', 'unidirectional']
print(sorted(set([''.join([char for char in word if char in 'aeiou']) for word in words])))
'''
words = [’attribution’, ’confabulation’, ’elocution’, ’sequoia’,’tenacious’, ’unidirectional’]
vsequences = set()
for word in words:
	vowels = []
 	for char in word:
 		if char in ’aeiou’:
 			vowels.append(char)
 	vsequences.add(’’.join(vowels))
sorted(vsequences)
[’aiuio’, ’eaiou’, ’eouio’, ’euoia’, ’oauaio’, ’uiieioa’]
'''