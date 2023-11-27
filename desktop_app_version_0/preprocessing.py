from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import re
import string
from nltk import pos_tag
from nltk.corpus import stopwords


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


def custom_string_splitter(input_string):
    # Define stop-words from nltk.corpus
    stop_words = set(stopwords.words('english'))

    # Define color_words, size_words, and multiplier_words
    color_words = {'red', 'blue', 'green', 'yellow', 'orange', 'wood-colored', 'purple', 'pink', 'white', 'gray', 'grey', 'brown', 'black', 'light', 'dark', 'leopard', 'metallic'}
    size_words = {'small', 'large', 'medium', 'big', 'tiny', 'enormous', 'little'}
    multiplier_words = {'single', 'double', 'triple', 'quadruple'}
    relative_pos = {'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'VBN', 'WDT'}
    defining_words = {'dressing', 'computer', 'ceiling', 'glass', 'bedside', 'full-wall', 'coffee', 'wall', 'partition', 'photo', 'bedtime', 'built-in', 'side', 'wall', 'floor', 'end'}

    # Split the input string into a list of words
    words = input_string.lower().split()

    # Initialize an empty list to store the result
    result = []

    # Initialize variables to store the current element and the previous word
    current_element = ""

    # Define functions to check if a word represents color, size, or is a number
    def is_color(word):
        return word in color_words

    def is_size(word):
        return word in size_words

    def is_number(word):
        return bool(re.match(r'\d+', word))

    def get_word_pos(word):
      tagged_word = pos_tag(word_tokenize(word))
      return tagged_word[0][1]

    def is_punctuation(token):
      return all(char in string.punctuation for char in token)

    # Iterate through the words in the input string
    for word in words:
        # Skip stop-words
        if word in stop_words:
            continue
        
        pos = get_word_pos(word)

        if is_punctuation(word):
            continue

        # Check the conditions specified in the rules
        if is_color(word) or is_size(word) or is_number(word) or word in multiplier_words or word in defining_words or pos in relative_pos or word.isdigit():
            current_element += " " + word
        else:
            # If the current word doesn't meet the conditions, start a new element
            if len(current_element) >= 1:
                current_element += " " + word
                result.append(current_element.strip())
                current_element = ""
            else:
                result.append(word)

    return result