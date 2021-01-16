import re

fp = open("sample.txt", "r", encoding="utf-8")
article = fp.read()
# print(article)
new_article = re.sub("[^a-zA-Z\s]", "", article)
# print(new_article)
words = new_article.split()
# print(words)
word_counts = {}
for word in words:
    if word.upper() in word_counts:
        word_counts[word.upper()] = word_counts[word.upper()] + 1
    else:
        word_counts[word.upper()] = 1
#
key_list = list(word_counts.keys())
key_list.sort()
for key in key_list:
    if word_counts[key] >= 1:
        print("{}:{}".format(key, word_counts[key]))