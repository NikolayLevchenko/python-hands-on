def search_for_vowels(phrase: str) -> set:
    """Returns the set of vowels found in 'phrase'."""
    return set('aeiou').intersection(set(phrase))


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Returns the set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', mode='a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
