"""
Iterating String with While
"""

phrase = 'I am learning Python!'
new_phrase = ''
phraseLen = len(phrase)
counter = 0
# print(phrase[0])

while counter < phraseLen:
    print(phrase[counter])
    new_phrase += phrase[counter]
    counter += 1

print(new_phrase)
