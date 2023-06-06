import random
import urllib.request
import sys

# Learning to Speak Object Oriented


# class - Tell Python to make a new kind of thing
# object - Two meanings: the most basic kind of thing, and any instance of some thing
# instance - What you get when you tell Python to create a class
# def - How you define a function inside a class
# self - Inside the functions in a class, self is a variable for the instance/object being accessed
# inheritance - the concept that one class can inherit traits from another class, much like you and    your parents
# composition - the concept that a class can be composed of other classes as parts much like how a car has wheels
# attribute - a property classes have that are from composition and are usually variables
# is-a - a phrase to say that something inherits from another, as in a "salmon" is-a "fish"
# has-a - a phrase to say that something is composed of other things or has a trait, as in "a salmon has-a mount"

""" Phrase Drills
 class X(Y) - "Make a class named X that is-a Y."
 class X(object): def __init__(self, J) "class X has-a __init__ that takes self and J parameters"
 class X(object): def M(self, J) "class X has-a function named M that takes self and J parameters"
 foo = X() "Set foo to an instance of class X"
 foo.M(J) "From foo, get the M function, and call it with parameters self, J"
 foo.K = Q "From foo get the K attribute and set it to Q"

"""

"""
1. "Make a class named ? that is-a Y."
2. "class ? has-a __init__ that takes self and ? parameters."
3. "class ? has-a function named ? that takes self and ? parameters."
4. "Set foo to an instance of class ?"
5. "From foo get the ? function and calls it with self=? and parameters ?"
6. "From foo get the ? attribute and set it to ?"

"""

req = urllib.request.Request("http://learncodethehardway.org/words.txt")
with urllib.request.urlopen(req) as response:
    WORD_URL = response.read()
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class name %%% that is-a %%%",
    "class %%%(object):\n\tdef ___init___(self, ***)":
        "class %%% has-a ___init___ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self,@@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters",
    "*** = %%%()":
        "Set *** to an instance of class %%%",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up the words from the website
for word in (WORD_URL).read():
    WORDS.append(word.strip())


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names

    for word in class_names:
        result = result.replace("%%%", word, 1)

    # fake other names
    for word in other_names:
        result = result.replace("***", word, 1)

    # fake parameter lists
    for word in param_names:
        result = result.replace("@@@", word, 1)

    results.append(result)

    return results


# keep going until they hit CTRL-D

try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            raw_input("> ")
            print("ANSWER: %s\n\n") % answer
except EOFError:
    print("\nBye")
