from flask import Flask, render_template, request, escape
from functions import help_functions

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(help_functions.search_for_letters(phrase, letters))
    help_functions.log_request(request, results)
    return render_template('results.html',
                           the_letters=letters,
                           the_phrase=phrase,
                           the_results=results
                           )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)


if __name__ == '__main__':
    app.run(debug=True)
