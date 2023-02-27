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
