#%%
import nltk
# download the data
# nltk.download()

messages = [line.rstrip() for line in open('SMSSpamCollection')]

print(len(messages))

for message_number, message in enumerate(messages[:10]):
    print(message_number, message)
    print('\n')

import pandas as pd

messages = pd.read_csv('SMSSpamCollection', sep='\t', names=['label', 'message'])

messages.head()

messages.describe()

messages.groupby('label').describe()

messages['length'] = messages['message'].apply(len)

messages.head()

import matplotlib.pyplot as plt
import seaborn as sns

messages['length'].plot.hist(bins=150)

messages[messages['length'] == 910]['message'].iloc[0]

messages.hist(bins=100, column='length', by='label', figsize=(12,4))

#preprocessing the data

import string

mess = 'Sample message! Notice: it has punctuation.'

# Check characters to see if they are in punctuation
nopunc = [char for char in mess if char not in string.punctuation]
nopunc = ''.join(nopunc)

from nltk.corpus import stopwords
# retirar as palavras mais comuns
stopwords.words('english')[0:10] # Show some stop words

clean_mess = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

def text_process(mess):
    # Check characters to see if they are in punctuation and remove them
    nopunc = [char for char in mess if char not in string.punctuation]
    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    # Now just remove any stopwords
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# Show original dataframe
messages.head()

# tokenization
messages['message'].head(5).apply(text_process)
# stemming
from sklearn.feature_extraction.text import CountVectorizer
bow_transformer = CountVectorizer(analyzer=text_process).fit(messages['message'])
print(len(bow_transformer.vocabulary_))
#%%

message4 = messages['message'][3]
print(message4)
bow4 = bow_transformer.transform([message4])
print(bow4)
print(bow4.shape)

#print(bow_transformer.get_feature_names()[9554])

#%%


