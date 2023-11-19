# -*- coding: utf-8 -*-
"""synonyms_for_user_input.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XOISV0fYaWWNPiiH5n5CxyjqGW7bFLTR
"""

# imports and uploads
# !pip install nltk
import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

from google.colab import files
files.upload()

with open('labelled_bedrooms_data_sample.txt.txt') as f:
    bedrooms_lines = f.readlines()

bedroom_files = []
for bedroom_line in bedrooms_lines:
    bedroom_files.append(bedroom_line.split("; ")[0])
bedrooms = []
for bedroom_line in bedrooms_lines:
    bedrooms.append(bedroom_line.split("; ")[2:])

def get_vector_representation(vector, nlp):
    vec = []
    for phrase in vector:
        tokens = nlp(phrase)
        for token in tokens:
            word = token.text
            if word in nlp.vocab:
                vec.extend(nlp(word).vector)
    return vec

!python -m spacy download en_core_web_lg
import spacy
nlp = spacy.load("en_core_web_lg")

# creating static inputs to test our program
user_string = 'Little bedroom with yellow double ottoman and light table and picture'.split()
user_input = 'Little bedroom with yellow double ottoman and light table and picture'
user_vec = get_vector_representation(user_string, nlp)

"""The following code looks for the synonims of inputed by a user words, if they are met more frequently in the labelled data (actually data was labbeled in a way to avoid synonyms, using only one term for same or similar items). If there is a synonym for the word, that is used in labelled data, but not in user's quiry, the code replaces the word in the user query with a synonym, found in labelled data."""

labeled_data_beds = [word for ngram in bedrooms for phrase in ngram for word in phrase.split()]

def replace_synonyms(user_input, labeled_words):
    tokens = word_tokenize(user_input)
    replaced_tokens = []
    for token in tokens:
        if token not in labeled_words:
            synonyms = set()
            for syn in wordnet.synsets(token):
                for lemma in syn.lemmas():
                    synonym = lemma.name().lower()
                    if synonym in labeled_words:
                        synonyms.add(synonym)
            if synonyms:
                replaced_tokens.append(synonyms.pop())
            else:
                replaced_tokens.append(token)
        else:
            replaced_tokens.append(token)

    replaced_text = ' '.join(replaced_tokens)
    return replaced_text

result = replace_synonyms(user_input, labeled_data_beds)
print(result)