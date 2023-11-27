import spacy
import nltk
import numpy as np

def calculate_cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def calculate_element_similarity(set1, set2):
    return len(set1 & set2) / len(set1 | set2)


def get_vector_representation(vector, nlp):
    vec = []
    for phrase in vector:
        tokens = nlp(phrase)
        for token in tokens:
            word = token.text
            if word in nlp.vocab:
                vec.extend(nlp(word).vector)
    return vec


def pad_vector(vector, dimension):
    return np.pad(vector, (0, dimension - len(vector)), 'constant')