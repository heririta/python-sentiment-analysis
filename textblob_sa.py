# https://www.analyticsvidhya.com/blog/2021/10/sentiment-analysis-with-textblob-and-vader/
# https://www.analyticsvidhya.com/blog/2021/10/sentiment-analysis-with-textblob-and-vader/


from textblob import TextBlob
from textblob import Word
# import nltk
# nltk.download('omw-1.4')


res = TextBlob("This movie is amazingly directed")
# print(res.sentiment.polarity)

my_sentence = TextBlob(
    "I am reading a blog post on AnalyticsVidhya. I am loving it!")

# PoS tagging. With POS or Part-of-speech tagging
print(my_sentence.tags)

# Noun Phrases using Textblob
print(my_sentence.noun_phrases)

# Sentiment Analysis using Textblob
print(my_sentence.sentiment)

# Tokenization using Textblob
# print(my_sentence.words)
print(my_sentence.sentences)

# Word Inflection using Textblob
print(my_sentence.words[4].pluralize())  # the word "blog"

# Lemmatization using Textblob
# Lemmatization is the process of aggregating together the derived forms of a word into a single element or item. The “lemmatize” property helps us achieve this functionality. In Natural Language Processing (NLP) and machine learning, lemmatization is one of the most used text techniques during the pre-processing phase.
w = Word("radii")
print(w.lemmatize())

w = Word("went")
print(w.lemmatize("v"))

# Definition using Textblob
print(Word("blog").definitions)

# Synsets
# The “synsets” property returns a list of synset objects for a particular word.
word = Word("phone")
print(word.synsets)

# Spelling Correction using Textblob
# The spell check operation is performed by the “correct()” method. It uses the classic approach of Peter Norvig’s “How to Write a Spelling Corrector?“
my_sentence = TextBlob("I am not in denger. I am the dyangr.")
print(my_sentence.correct())

# Similarly, the `spellcheck()` method returns a list of probably correct words along with the confidence in the form of a tuple.
w = Word('neumonia')
print(w.spellcheck())

# Word frequencies using Textblob
# The “word_counts” operation returns the number of counts of a particular word in the sentence.
betty = TextBlob("Betty Botter bought some butter. But she said the Butter’s bitter. If I put it in my batter, it will make my batter bitter. But a bit of better butter will make my batter better.")
print(betty.word_counts['butter'])
# To apply the case sensitiveness, we can apply the `.count(word, case_sensitive=True)` operations.
print(betty.words.count('butter', case_sensitive=True))

# Parsing using TextBlob
print(betty.parse())

# Similarities of TextBlob with Python string
# TextBlobs are similar to Python strings. They can perform basic slicing operations just like the regular Python strings.
my_sentence = TextBlob("Simple is better than complex.")
print(my_sentence[0:16])
# Apart from slicing, the “upper()” and “lower()” can also be implemented.
print(my_sentence.upper())
# And just like the regular string, we can also perform the “find()” operation.
print(my_sentence.find("better"))
# Textblobs and Python strings can easily be concatenated.
a = TextBlob("Black")
b = TextBlob("Blue")
print(a + ' and ' + b)
# The object can also be formatted.
print("{0} and {1}".format(a, b))

# N-gram using TextBlob
# Consider the following examples:
# 1) A cat is in the bag.
# 2) Say my name.
# 3) Good luck
# An N-gram is simply the sequence of ‘n’ words. In the above example, the first statement “A cat is in the bag” is a 6-gram. Likewise, “Say my name” is 3-gram, and “Good luck” is 2-gram. N-grams are utilized for a wide range of tasks. When creating a language model, for example, n-grams are utilized to create not only unigram (single n-gram) models but also bigram (2-gram) and trigram (3-gram) or multiple models.
bob = TextBlob(
    "How many roads should a man must walk before we can call him a man?")
print(bob.ngrams(n=3))



# Basic Guides

# – POS Tagging

# – Noun Phrases

# – Sentiment Analysis

# – Tokenization

# – Word Inflection

# – Lemmatization

# – Definition

# – Synsets

# – Word frequencies

# – Parsing

# – Similarities with Python string

# – N-gram