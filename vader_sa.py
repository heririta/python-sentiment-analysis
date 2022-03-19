from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# sid_obj = SentimentIntensityAnalyzer()
# print(sid_obj.polarity_scores("no slow motion camera"))

# https://www.analyticsvidhya.com/blog/2021/10/sentiment-analysis-with-textblob-and-vader/
# https://www.analyticsvidhya.com/blog/2021/06/vader-for-sentiment-analysis/

# function to print sentiments
# of the sentence.


def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
# polarity_scores method of SentimentIntensityAnalyzer
# oject gives a sentiment dictionary.
# which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
    print("Sentence Overall Rated As", end=" ")
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")
    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")
    else:
        print("Neutral")


# Driver code
if __name__ == "__main__":
    print("Text Selected for VADER Sentimental Analysis :")
    sentence1 = ('''ANN is like our brain; millions and billions of cells — called neurons, which processes information in the form of electric signals. Similarly, in ANN, the network structure has an input layer, a hidden layer, and the output layer. It is also called Multi-Layer Perceptron as it has multiple layers. The hidden layer is known as a “distillation layer” that distils some critical patterns from the data/information and passes it onto the next layer. It then makes the network quicker and more productive by distinguishing the data from the data sources, leaving out the excess data.''')
    print(sentence1)

# function calling
sentiment_scores(sentence1)
