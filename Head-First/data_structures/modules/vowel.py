person3 = {"Name": "Ford Prefect", "Gender": "Male", "Occupation": "Researcher", "Home Planet": "Betelgeuse Seven",
           'Age': 33}

# print(person3)

vowels = ['a', 'e', 'i', 'o', 'u']
found = {'o': 0, 'u': 0, 'a': 0, 'i': 0, 'e': 0}
flag = False

word = input("Provide a word to search for and count vowels...")

for i in word:
    if i in vowels:
        flag = True
        found[i] += 1

# for k in sorted(found):
#     print(k, 'was found', found[k], 'time(s)')
if flag:
    for k, v in sorted(found.items()):
        print(k, 'was found', v, 'time(s).')




