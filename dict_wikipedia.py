import wikipedia 
import re, time
from typing import List

def tokenize(text: str) -> List[str]:
    """Splits given text into a list of the individual tokens in order

    Args:
        text - text to tokenize

    Returns:
        tokens of given text in order
    """
    tokens = []
    token = ""
    for c in text:
        if (
            re.match("[a-zA-Z0-9]", str(c)) != None
            or c == "'"
            or c == "_"
            or c == "-"
        ):
            token += c
        else:
            if token != "":
                tokens.append(token.lower())
                token = ""
            
    if token != "":
        tokens.append(token.lower())
    return tokens


article = wikipedia.page("Artemis II", auto_suggest=False).content
#print(article)
tokens = tokenize(article)
print(tokens)

with open("sorted_stoplist.txt", "r", encoding='utf8') as f:
    stoplist = f.read()

stoplist_tokenized = tokenize(stoplist)
print(stoplist_tokenized)

freqs = {}

for word in tokens:
    if word not in stoplist_tokenized:
        if word in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1
#print(freqs)

#print total unique words and total number of words
unique_words = len(freqs)
total_num_words = sum(freqs.values())
print(f"Total Unique Words: {unique_words}")
print(f"Total Number of Words: {total_num_words}")

print()

#print the top 20
top_words = sorted(freqs.items(), key=lambda x: x[1], reverse=True)

for word, count in top_words[:20]:
    print(f" {word}: {count}")