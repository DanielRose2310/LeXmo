import pandas as pd
from nltk import word_tokenize
from LeXmo.loader import fetch_data

stemmer, emolex_words, emotions = fetch_data()

def run(text):

    '''
      Takes text and adds if to a dictionary with 10 Keys  for each of the 10 emotions in the NRC Emotion Lexicon,
      each dictionay contains the value of the text in that emotions divided to the text word count
      INPUT: string
      OUTPUT: dictionary with the text and the value of 10 emotions


      '''
   
    LeXmo_dict = {'text': text, 'anger': [], 'anticipation': [], 'disgust': [], 'fear': [], 'joy': [], 'negative': [],
                  'positive': [], 'sadness': [], 'surprise': [], 'trust': []}

    document = word_tokenize(text)

    word_count = len(document)
    rows_list = []
    for word in document:
        word = stemmer.stem(word.lower())

        emo_score = (emolex_words[emolex_words.word == word])
        rows_list.append(emo_score)

    df = pd.concat(rows_list)
    df.reset_index(drop=True)

    for emotion in list(emotions):
        LeXmo_dict[emotion] = df[emotion].sum() / word_count

    return LeXmo_dict
