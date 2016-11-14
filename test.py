from segmentation import segmentation

s = segmentation()

with open('sample.txt', 'r') as f:
    string = f.read()
    print(s.split_words(string))
