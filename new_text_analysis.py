import nltk.corpus
import string

nltk.download('words')
english_vocab = set(w.lower() for w in nltk.corpus.words.words())

with open("20200419-Danish-words.txt", "r") as f:
    danish_text = f.read()

danish_vocab = set(word.lower() for word in danish_text.splitlines() if word)

with open('test_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

tokens = [word.strip(string.punctuation).lower() for word in text.split() if word.isalpha()]

english_only = [w for w in tokens if w in english_vocab and w not in danish_vocab]

ambiguous_words = [w for w in tokens if w in english_vocab and w in danish_vocab]

print("English-only words found:", set(english_only))
print("Possible false friends:", set(ambiguous_words))