import sentiment_analysis as sa

example_sentence = "I hate this movie"

# get the sentiment
sentiment = sa.get_sentiment(example_sentence)

# print the sentiment
print(sentiment)

# output should be: -1