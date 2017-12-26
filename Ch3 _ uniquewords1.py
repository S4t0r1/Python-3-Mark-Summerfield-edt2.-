import string
import sys

words = {}
strip = string.digits + string.punctuation + string.whitespace + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().strip():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] = words.get(word, 0) + 1
for word in sorted(words):
    print("Word {0} found {1} times.".format(word, words[word]))
