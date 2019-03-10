# from random import randint
#
# wait_time = randint(1, 60)
# print(wait_time)

vowels = ['a', 'e', 'i', 'o', 'u']
found = []


def print_list(list):
    for i in list:
        print(i)


def letters_finder(word):
    for i in word:
        if i in vowels and i not in found:
            found.append(i)
    return print_list(found)


letters_finder("Boriska")
