import re
import xml.etree.ElementTree as etree

words = [
"awkward",
"back",
"backed",
"background",
"backing",
"hey",
"hi",
"what",
"whats",
"name",
"my",
"is",
"am",
"are",
"was",
"were",
"there",
"cat",
"cats",
"in",
"the",
"hat",
"no",
"she",
"playing",
"with",
"*article",
"a",
"an",
"the",
"*pronoun",
"you",
"he",
"she",
"i",
"my",
"they",
#add all words present in the language here.
]

test_string = "thecatinthehat"

def segment_words(test_string, result):
    # test for all possible prefixes
    for i in range(0, len(test_string)+1):
        # get substring from 0 to i in prefix to check in dict
        prefix = test_string[:i]
        #print(prefix)
        if prefix in words:
            # if entire string is tested, end and print
            if i == len(test_string):
                result += prefix
                print(result)
                return
            #recursive call with the remaining substring and updated result
            segment_words(test_string[i:len(test_string)], result+prefix+" ")

#segment_words(test_string, "")

def remove_extra(string):
    pass

with open('sample.txt', 'r') as f:
    string = f.read()
print(repr(string))