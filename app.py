import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
nltk.download('subjectivity')
nltk.download('movie_reviews')

analyzer = SentimentIntensityAnalyzer()

while True:
  next_message = input('Enter a message to check the sentiment: ')
  scores = analyzer.polarity_scores(next_message)

  compound = scores['compound']
  if compound > 0.1:
    print('Positive comment! \n')
  elif compound < -0.1:
    print('Negative comment! \n')
  else:
    print('Neutral comment! \n')