"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for
this week. E.g. the word "calling" means something in a programming context,
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ["what", "does", "this", "line", "do", "?"]

# I think this will print every for in some word
for word in some_words:
    print(word)  # this prints every word in some_words each on a new line

# I think this will print every word in the list some_words
for x in some_words:
    print(x)  # this prints every word in some_words each on a new line

# I think this will print the entire list of some_words
print(some_words)  # this prints the entire list on one line

# I think this will print if the size of the list some_words contains 3 or more values
if len(some_words) > 3:
    print(
        "some_words contains more than 3 words"
    )  # This prints "some_words contains more than 3 words" if the size of some_words is greater than 3.


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()
