from data_loader import load_files
from preprocessing import replace_synonyms, custom_string_splitter
from similarities import calculate_cosine_similarity, calculate_element_similarity, get_vector_representation, pad_vector
import numpy as np
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import re
import string
from nltk.corpus import stopwords
from nltk import pos_tag
import os
import spacy


def main():
    bedroom_files, bedrooms, living_rooms_files, living_rooms, kitchens_files, kitchens, dining_files, dining, bathroom_files, bathrooms = load_files()
    os.system("python -m spacy download en_core_web_lg")
    # nlp = spacy.load("models\en_core_web_lg\en_core_web_lg-3.7.1")
    nlp = spacy.load("en_core_web_lg")    
    nltk.download('wordnet')
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')

    room_input = input("Write down what you want to describe (bedroom, living room, dining room, kitchen, bathroom): ")
    if room_input in ['bedroom', 'living room', 'dining room', 'kitchen', 'bathroom']:
        user_input = input("Write a prompt for your room: ")
    else:
        print("Error! Write down something of the following: bedroom, living room, dining room, kitchen, bathroom")

    if room_input == 'bedroom':
        labeled_data_beds = [word for ngram in bedrooms for phrase in ngram for word in phrase.split()]
        user_input = replace_synonyms(user_input, labeled_data_beds)
        user_string = custom_string_splitter(user_input)
        user_vec = get_vector_representation(user_string, nlp)
        vecs_bedrooms = []
        max_dimension = 0
        for i in range(len(bedrooms)):
            vector = get_vector_representation(bedrooms[i], nlp)
            if len(vector) > max_dimension:
                max_dimension = len(vector)
            vecs_bedrooms.append(vector)
        for i in range(len(vecs_bedrooms)):
            if max_dimension < len(user_vec):
                max_dimension = len(user_vec)
            vecs_bedrooms[i] = pad_vector(vecs_bedrooms[i], max_dimension)
        user_vec = pad_vector(user_vec, max_dimension)
        element_similarities = []
        vector_similarities = []
        for i in range(len(vecs_bedrooms)):
            element_similarities.append(calculate_element_similarity(set(user_vec), set(vecs_bedrooms[i])))
            vector_similarities.append(calculate_cosine_similarity(user_vec, vecs_bedrooms[i]))
        overall_similarities = [0.5 * vector_sim + 0.5 * element_sim for vector_sim, element_sim in zip(vector_similarities, element_similarities)]
        top_indices = sorted(range(len(overall_similarities)), key=lambda i: overall_similarities[i], reverse=True)[:3]
        for idx in top_indices:
            print(f"Similarity: {overall_similarities[idx]}, File Name: {bedroom_files[idx]}")

    elif room_input == 'living room':
        labeled_data_liv = [word for ngram in living_rooms for phrase in ngram for word in phrase.split()]
        user_input = replace_synonyms(user_input, labeled_data_liv)
        user_string = custom_string_splitter(user_input)
        user_vec = get_vector_representation(user_string, nlp)
        vecs_living = []
        max_dimension = 0
        for i in range(len(living_rooms)):
            vector = get_vector_representation(living_rooms[i], nlp)
            if len(vector) > max_dimension:
                max_dimension = len(vector)
            vecs_living.append(vector)
        for i in range(len(vecs_living)):
            if max_dimension < len(user_vec):
                max_dimension = len(user_vec)
            vecs_living[i] = pad_vector(vecs_living[i], max_dimension)
        user_vec = pad_vector(user_vec, max_dimension)
        element_similarities = []
        vector_similarities = []
        for i in range(len(vecs_living)):
            element_similarities.append(calculate_element_similarity(set(user_vec), set(vecs_living[i])))
            vector_similarities.append(calculate_cosine_similarity(user_vec, vecs_living[i]))
        overall_similarities = [0.5 * vector_sim + 0.5 * element_sim for vector_sim, element_sim in zip(vector_similarities, element_similarities)]
        top_indices = sorted(range(len(overall_similarities)), key=lambda i: overall_similarities[i], reverse=True)[:3]
        for idx in top_indices:
            print(f"Similarity: {overall_similarities[idx]}, File Name: {living_rooms_files[idx]}")


    elif room_input == 'kitchen':
        labeled_data_kit = [word for ngram in kitchens for phrase in ngram for word in phrase.split()]
        user_input = replace_synonyms(user_input, labeled_data_kit)
        user_string = custom_string_splitter(user_input)
        user_vec = get_vector_representation(user_string, nlp)
        vecs_kitchens = []
        max_dimension = 0
        for i in range(len(kitchens)):
            vector = get_vector_representation(kitchens[i], nlp)
            if len(vector) > max_dimension:
                max_dimension = len(vector)
            vecs_kitchens.append(vector)
        for i in range(len(vecs_kitchens)):
            if max_dimension < len(user_vec):
                max_dimension = len(user_vec)
            vecs_kitchens[i] = pad_vector(vecs_kitchens[i], max_dimension)
        user_vec = pad_vector(user_vec, max_dimension)
        element_similarities = []
        vector_similarities = []
        for i in range(len(vecs_kitchens)):
            element_similarities.append(calculate_element_similarity(set(user_vec), set(vecs_kitchens[i])))
            vector_similarities.append(calculate_cosine_similarity(user_vec, vecs_kitchens[i]))
        overall_similarities = [0.5 * vector_sim + 0.5 * element_sim for vector_sim, element_sim in zip(vector_similarities, element_similarities)]
        top_indices = sorted(range(len(overall_similarities)), key=lambda i: overall_similarities[i], reverse=True)[:3]
        for idx in top_indices:
            print(f"Similarity: {overall_similarities[idx]}, File Name: {kitchens_files[idx]}")


    elif room_input == 'bathroom':
        labeled_data_bath = [word for ngram in bathrooms for phrase in ngram for word in phrase.split()]
        user_input = replace_synonyms(user_input, labeled_data_bath)
        user_string = custom_string_splitter(user_input)
        user_vec = get_vector_representation(user_string, nlp)
        vecs_bathrooms = []
        max_dimension = 0
        for i in range(len(bathrooms)):
            vector = get_vector_representation(bathrooms[i], nlp)
            if len(vector) > max_dimension:
                max_dimension = len(vector)
            vecs_bathrooms.append(vector)
        for i in range(len(vecs_bathrooms)):
            if max_dimension < len(user_vec):
                max_dimension = len(user_vec)
            vecs_bathrooms[i] = pad_vector(vecs_bathrooms[i], max_dimension)
        user_vec = pad_vector(user_vec, max_dimension)
        element_similarities = []
        vector_similarities = []
        for i in range(len(vecs_bathrooms)):
            element_similarities.append(calculate_element_similarity(set(user_vec), set(vecs_bathrooms[i])))
            vector_similarities.append(calculate_cosine_similarity(user_vec, vecs_bathrooms[i]))
        overall_similarities = [0.5 * vector_sim + 0.5 * element_sim for vector_sim, element_sim in zip(vector_similarities, element_similarities)]
        top_indices = sorted(range(len(overall_similarities)), key=lambda i: overall_similarities[i], reverse=True)[:3]
        for idx in top_indices:
            print(f"Similarity: {overall_similarities[idx]}, File Name: {bathroom_files[idx]}")


    elif room_input == 'dining room':
        labeled_data_din = [word for ngram in dining for phrase in ngram for word in phrase.split()]
        user_input = replace_synonyms(user_input, labeled_data_din)
        user_string = custom_string_splitter(user_input)
        user_vec = get_vector_representation(user_string, nlp)
        vecs_dining = []
        max_dimension = 0
        for i in range(len(dining)):
            vector = get_vector_representation(dining[i], nlp)
            if len(vector) > max_dimension:
                max_dimension = len(vector)
            vecs_dining.append(vector)
        for i in range(len(vecs_dining)):
            if max_dimension < len(user_vec):
                max_dimension = len(user_vec)
            vecs_dining[i] = pad_vector(vecs_dining[i], max_dimension)
        user_vec = pad_vector(user_vec, max_dimension)
        element_similarities = []
        vector_similarities = []
        for i in range(len(vecs_dining)):
            element_similarities.append(calculate_element_similarity(set(user_vec), set(vecs_dining[i])))
            vector_similarities.append(calculate_cosine_similarity(user_vec, vecs_dining[i]))
        overall_similarities = [0.5 * vector_sim + 0.5 * element_sim for vector_sim, element_sim in zip(vector_similarities, element_similarities)]
        top_indices = sorted(range(len(overall_similarities)), key=lambda i: overall_similarities[i], reverse=True)[:3]
        for idx in top_indices:
            print(f"Similarity: {overall_similarities[idx]}, File Name: {dining_files[idx]}")


    else:
        print("Error! Unsupported room type")

if __name__ == "__main__":
    main()