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

tree = etree.parse('dict.xml')
root = tree.getroot()
# for child in root:
#     for n in child:
#         print(n.text)


test_string = "thecatisinthebat"

def segment_words(test_string, result):
    # test for all possible prefixes
    for i in range(0, len(test_string)+1):
        # get substring from 0 to i in prefix to check in dict
        prefix = test_string[:i]
        print(prefix)
        if prefix in words:
            # if entire string is tested, end and print
            if i == len(test_string):
                result += prefix
                print(result)
                return
            #recursive call with the remaining substring and updated result
            segment_words(test_string[i:len(test_string)], result+prefix+" ")

#segment_words(test_string, "")
final = []
def segment_words_xml(test_string, result):
    global final
    # test for all possible prefixes
    for i in range(0, len(test_string)+1):
        # get substring from 0 to i in prefix to check in dict
        prefix = test_string[:i]
        #print(prefix)
        for token in root:
            for entry in token:
                if prefix == entry.text:
                    # if entire string is tested, end and print
                    if i == len(test_string):
                        result += prefix
                        final = result
                        #print(result)
                        #print(final)
                        #print(result)
                        return# final
                    #recursive call with the remaining substring and updated result
                    segment_words_xml(test_string[i:len(test_string)], result+prefix+" ")
    #return final

def remove_extra(string_list):
    size = len(string_list)
    i = 0
    while i < size:
        g = re.findall(r'[um]+|[hm]+', string_list[i], re.IGNORECASE)
        for j in range(len(g)):
            #print(g)
            if g[j] in string_list:
                string_list.remove(g[j])
                size -= 1
        i += 1
    return string_list

def remove_punctuation(string_list):
    size = len(string_list)
    i = 0
    while i < size:
        g = re.findall(r'[.,!?]+', string_list[i], re.IGNORECASE)
        for j in range(len(g)):
            #print(g)
            if g[j] in string_list[i]:
                string_list[i] = string_list[i].replace(g[j],"")
        i += 1
    return string_list

def segment(string_list):
    for i in range(len(string_list)):
        exists = False
        for token in root:
            for entry in token:
                if string_list[i] == entry.text:
                    exists = True
        if exists == False:
            print(string_list[i])
            result = segment_words_xml(string_list[i], "")
            print(result)
    return string_list

def stupid_segment(string_list):
    for i in range(len(string_list)):
        if len(string_list[i]) > 10:
            segment_words_xml(string_list[i], "")
            l = []
            l = re.split(' ', final)
            del string_list[i]
            string_list.extend(l)
    return string_list

def split_words(test_string):
    #test_string = remove_punctuation(test_string)
    string_list = re.split('[\r\n:\' \']+' , test_string)
    #string_list = re.split('[\s:]+' , test_string)
    print(len(string_list))
    string_list = remove_punctuation(string_list)
    string_list = remove_extra(string_list)
    string_list = stupid_segment(string_list)
    print(len(string_list))
    return string_list

with open('sample.txt', 'r') as f:
    string = f.read()
    print(split_words(string))