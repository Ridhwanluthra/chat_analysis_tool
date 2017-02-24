from segmentation import segmentation

s = segmentation()
# word_list = []
with open('sample.txt', 'r') as f:
    global word_list
    string = f.read()
    word_list = s.split_words(string)
    print(word_list)
    # for i in range(len(word_list)):
    #     exists = False
    #     for token in s.root:
    #         for entry in token:
    #             if word_list[i] == entry.text:
    #                 exists = True
    #     if exists == False:
    #         print(word_list[i])
