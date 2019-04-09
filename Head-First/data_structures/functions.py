def print_my_vowels(phrase: str) -> set:
    """the function returns a set of vowels from the string you've entered"""
    vowels = set('aeiou')
    found = vowels.intersection(set(phrase))
    return found


def search_for_letters(phrase: str, letters: str) -> set:
    """the function returns a set of letters found in 'phrase'."""
    found = set(letters).intersection(set(phrase))
    return found


print(search_for_letters('give me an example of your high performance', 'qwertyuio'))
