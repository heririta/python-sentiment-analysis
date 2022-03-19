# Passing the string text into word tokenize for bre
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import LancasterStemmer
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import nltk
import nltk.corpus

# For NLP, I am using my own statement as if I would use the dataset, it will be a very lengthy analysis.
text = "In Brazil they drive on the right-hand side of the road. Brazil has a large coastli"

# Now, from the library nltk.tokenize import word_tokenize as:
token = word_tokenize(text)
print(token)

# finding the frequency distinct in the tokens
# Importing FreqDist library from nltk and passing token into FreqDist
fdist = FreqDist(token)
print(fdist)

# To find the frequency of top 10 words
fdist1 = fdist.most_common(10)
print(fdist1)

# For stemming, we will import PorterStemmer and LancasterStemmer, these are the two methods from which we can perform the stemming procedure.
# Importing Porterstemmer from nltk library
# Checking for the word ‘waiting’
pst = PorterStemmer()
print(pst.stem("waiting"))

# Importing LancasterStemmer from nltk
lst = LancasterStemmer()
stm = ["giving", "given", "given", "gave"]
for word in stm:
    print(word + ":" + lst.stem(word))

# Importing Lemmatizer library from nltk
lemmatizer = WordNetLemmatizer()
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))

# After Lemmatization, we have to identify Stop Words. Stop words are nothing but the articles used in the English language like “the”, “a”, “at”, “for”, “above”, “on”, “is”, “all”.
# Articles don’t have any meaning while performing sentimental analysis as we cannot conclude anything from “the”, “a”, “at”, “for”, “above”, “on”, “is”, “all”. The system will look for the words that have some meaning in identifying a product/service like ‘Good’, ‘Bad’ or ‘Great’.
# importing stopwords from nltk library

nltk.download('stopwords')

a = set(stopwords.words('english'))
text = "Cristiano Ronaldo was born on February 5, 1985, in Funchal, Madeira, Portugal."
text1 = word_tokenize(text.lower())
print(text1)
stopwords = [x for x in text1 if x not in a]
print(stopwords)

# After this,
# We have to make the system understand that what all words are ‘nouns’, ‘pronouns’, etc., for better analysis.
# It is known as Part of Speech Tagging (POS)
# For example, I will use a sentence:
text = "vote to choose a particular man or a group (party) to represent them in parliament"
# Tokenize the text
tex = word_tokenize(text)
for token in tex:
    print(nltk.pos_tag([token]))


# After POS, we have to do the Named entity Recognition step
# It is the step in which the system identifies which word is a person’s name, location, etc.
# For this, your system should have Ghostscript installed in the file where you have installed python3.
# For this step, from nltk import ne_chunk as it helps in giving a tree-like structure to the output so that it will be easily understandable for us.

from nltk import ne_chunk# tokenize and POS Tagging before doing chunk
text = "vote to choose a particular man or a group (party) to represent them in parliament"
#importing chunk library from nltk
token = word_tokenize(text)
tags = nltk.pos_tag(token)
chunk = ne_chunk(tags)
chunk

# After this, Chunking took place, i.e., grouping the individual piece of information into bigger pieces.
# For example, I have used:

text = "We saw the yellow dog"
token = word_tokenize(text)
tags = nltk.pos_tag(token)
reg = "NP: {<DT>?<JJ>*<NN>}"
a = nltk.RegexpParser(reg)
result = a.parse(tags)
print(result)