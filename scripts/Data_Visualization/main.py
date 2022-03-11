import pandas as pd
from pie_chart import *
from histogram import *
from word_cloud import *

data = pd.read_csv('RAW_recipes.csv')
data2 = pd.read_csv('RAW_interactions.csv')

pie_chart(data, data2)
histogram(data)
word_cloud(data2)