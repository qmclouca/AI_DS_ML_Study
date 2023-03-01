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

messages_bow = bow_transformer.transform(messages['message'])
sparsity = (100.0 * messages_bow.nnz / (messages_bow.shape[0] * messages_bow.shape[1]))
print('sparsity: {}'.format(sparsity))

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer().fit(messages_bow)
tfidf4 = tfidf_transformer.transform(bow4)
print(tfidf4)
print(tfidf_transformer.idf_[bow_transformer.vocabulary_['u']])
print(tfidf_transformer.idf_[bow_transformer.vocabulary_['university']])
messages_tfidf = tfidf_transformer.transform(messages_bow)
print(messages_tfidf.shape)
from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(messages_tfidf, messages['label'])
print('predicted:', spam_detect_model.predict(tfidf4)[0])
print('expected:', messages.label[3])

from sklearn.model_selection import train_test_split

msg_train, msg_test, label_train, label_test = \
train_test_split(messages['message'], messages['label'], test_size=0.3)

print(len(msg_train), len(msg_test), len(msg_train) + len(msg_test))

from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),  # strings to token integer counts
    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
])

pipeline.fit(msg_train,label_train)

predictions = pipeline.predict(msg_test)

from sklearn.metrics import classification_report
print(classification_report(predictions,label_test))



#%%


