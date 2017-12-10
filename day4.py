file = open('input-day4.txt','r')
sum = 0

for line in file.readlines():
    ha = set()
    valid = True
    for word in line.split():
        if word in ha:
            valid = False
        else:
            ha.add(word)
    if valid:
        sum = sum + 1

print sum

import itertools

file = open('input-day4.txt','r')
sum = 0

for line in file.readlines():
    ha = set()
    valid = True
    for word in line.split():
        anagrams = set(itertools.permutations(word))
        for anagram in anagrams:
            if str(anagram) in ha:
                valid = False
            else:
                ha.add(str(anagram))
    if valid:
        sum = sum + 1

print sum
