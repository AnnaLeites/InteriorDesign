import streamlit as st 
from gensim.models import Word2Vec
import multiprocessing
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string



def load_data():
    #read data
    with open('labelled_bedrooms_data_sample.txt.txt') as f:
        bedrooms_lines = f.readlines()
    with open('labelled_living_rooms_data_sample.txt.txt') as f:
        living_rooms_lines = f.readlines()


    #adding all bedrooms and living rooms to list of vectors and to list of filenames
    rooms_files = []
    rooms = []

    for bedroom_line in bedrooms_lines:
        rooms_files.append(bedroom_line.split("; ")[0])
        rooms.append(bedroom_line.split("; ")[1:])

    for living_room_line in living_rooms_lines:
        rooms_files.append(living_room_line.split("; ")[0])
        rooms.append(living_room_line.split("; ")[1:])
        
    return rooms_files, rooms

def get_embedding(sentence,w2v_model):
    vectors = []
    for word in sentence:
        if word in w2v_model.wv.index_to_key:
            vector = w2v_model.wv[word]
            vectors.append(vector)
    #embedding of the whole sentence is average vector        
    sentence_embedding = np.mean(vectors, axis=0)
    return sentence_embedding

def get_w2v_model(rooms):
    #word to vec CBOW
    cores = multiprocessing.cpu_count() 
    w2v_model = Word2Vec(min_count=2,
                         window=2,
                         sg = 0,
                         sample=6e-5, 
                         alpha=0.03, 
                         min_alpha=0.0007, 
                         negative=20,
                         workers=cores-1)
    w2v_model.build_vocab(rooms)
    return w2v_model



    #the mothods creating embeddigs for the whole dataset
def create_embeddings():
    rooms_files, rooms = load_data()
    create_embeddings._w2v_model = get_w2v_model(rooms)
    
    embeddings_of_sentences = []
    for room in rooms:
        sentence_embedding = get_embedding(room,create_embeddings._w2v_model)
        embeddings_of_sentences.append(sentence_embedding)
    return embeddings_of_sentences, rooms_files

def get_prompt_embedding(prompt,w2v_model):
    text = prompt.lower()
    
    # tokenization
    tokens = word_tokenize(text)
    
    # delete stop_words
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    prompt_embedding = get_embedding(tokens,w2v_model)
    
    return prompt_embedding

# Function to calculate cosine similarity between two vectors
def calculate_cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))



#st.header("Please choose one of the options to generate design of your room")
st.header("Please write the text to generate design of your room")




col1, col2 = st.columns(2)

with col1:
   st.header("Text to Room generator")
   
   col11, col12 = st.columns(2)
   with col11:
       input_prompt = st.text_input("Input detailed description of the room") 
   with col12:
       if st.button("OK", type="primary"):
           embeddings_of_sentences, rooms_files = create_embeddings()
           prompt_embedding = get_prompt_embedding(input_prompt, create_embeddings._w2v_model)
           similiarity = calculate_cosine_similarity(embeddings_of_sentences, prompt_embedding)
           file = str(rooms_files[np.argmax(similiarity)])
           st.text(file)
           col2 = st.image(file)


#with col2:
  # st.header("Room to Room generator")
   #st.write("Upload a photo of your room")
  # upload_file = st.file_uploader(label="Choose a image file ")    
  # if upload_file:

      #  img = upload_file.read()
      #  content_img=  upload_file.name
      #  #content_img= image_to_data_url(content_img, img)
       # st.info("Uploaded Image")
       # st.image(img, width=300)
