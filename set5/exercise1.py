# -*- coding: UTF-8 -*-

import requests

"""REFACTORING

Refactoring is the process of making your code better. You are usually looking
to make it more readable or easier to maintain. Usually you'll do this by
pulling out bits of code that encapsulate one idea, especially if that idea is
used in several places.

We've talked already about
    ↱red→green→refactor↴
    ↜←←←←←←←←←←←←←←←←←←↩

Where red means make sure the test fails if you haven't done anything, green
means make the test pass, however you can, now this is the refactor part.

The function below works fine, but it's long and hard to read. Identify the
parts that are repeated, and pull them out into their own functions. I've made
that easier for you by making the function stubs for the bits you need to do.

Modify this function, don't write a whole new one.
"""


def wordy_pyramid():
    list_of_lengths = list(range(3, 21, 2)) + list(range(20, 3, -2))
    pyramid_list = list_of_words_with_lengths(list_of_lengths)
    return pyramid_list


def get_a_word_of_length_n(length):
    URL = 'https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength='+str(length)
    r = requests.get(URL)
    if r.status_code == 200:
            return r.text
    else:
        print("failed a request", r.status_code)


def list_of_words_with_lengths(list_of_lengths):
    list_of_words = []
    for length in list_of_lengths:
        list_of_words.append(get_a_word_of_length_n(length))
    return list_of_words


if __name__ == "__main__":
    pyramid = wordy_pyramid()
    for word in pyramid:
        print(word)
