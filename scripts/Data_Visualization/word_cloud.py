import pandas as pd
import matplotlib.pyplot as plt
import string
import re
from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords

def word_cloud(data):
    rating = data.loc[data.rating == 5]
    review = rating['review'].tolist()
    review = [x for x in review if pd.isnull(x) == False]
    review = [re.sub('[\d]', '', i) for i in review]
    review = [re.sub('[{}]'.format(string.punctuation), "", i) for i in review]
    review = ' '.join(review)
    with open('data.txt', 'w') as f:
        f.write(review)
    text = open('data.txt').read()
    stop_words = set(stopwords.words('english'))
    s = ['recipe', 'make', 'made', 'used', 'Thank', 'added', 'one', 'posting',
         'lot', 'bit', 'put', 'Thanks', 'use', 'next', 'time', 'will', 'think',
         'making', 'add', 'much', 'little', 'sharing', 'turned', 'didnt', 'instead',
         'half', 'would', 'maybe', 'still']
    new_stopwords_list = stop_words.union(s)
    wordcloud = WordCloud(stopwords=new_stopwords_list, background_color='black', max_words=1000000)
    process_word = WordCloud.process_text(wordcloud, str(text))
    wordcloud.generate_from_frequencies(process_word)
    image = wordcloud.to_image()
    plt.figure(figsize=(15, 10))
    plt.imshow(image)
    plt.axis('off')
    plt.savefig('wordcloud.png')
    plt.show()

data = pd.read_csv('RAW_interactions.csv')
word_cloud(data)