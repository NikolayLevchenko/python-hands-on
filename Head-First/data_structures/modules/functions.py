def print_my_vowels(phrase: str) -> set:
    """the function returns a set of vowels from the string you've entered"""
    vowels = set('aeiou')
    found = vowels.intersection(set(phrase))
    return found


# making function use a default value and be more generic
def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """the function returns a set of letters found in 'phrase'."""
    found = set(letters).intersection(set(phrase))
    return found


# print(search_for_letters('give me an example of your high performance'))
#
# print(search_for_letters(letters='aeiou', phrase="Let's go play basketball"))

def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)


numbers = [23, 25, 93]

change(numbers)
print(numbers)