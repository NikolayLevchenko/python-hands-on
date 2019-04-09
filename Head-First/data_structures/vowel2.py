vowels = ['a', 'e', 'i', 'o', 'u']
found = {'o': 0, 'u': 0, 'a': 0, 'i': 0, 'e': 0}

word = input("Provide a word to search for and count vowels...")

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
