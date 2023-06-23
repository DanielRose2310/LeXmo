import nltk
if not nltk.stem.snowball:
    nltk.download('punkt')
from nltk.stem.snowball import SnowballStemmer
import pandas as pd
from LeXmo.settings import lexicon,lex_dir

def fetch_data(lang='english'):

    emolex_df = pd.read_csv(f'{lex_dir}{lexicon}',
                            names=["word", "emotion", "association"],
                            sep=r'\t', engine='python')

    emolex_words = emolex_df.pivot(index='word',
                                    columns='emotion',
                                    values='association').reset_index()
    emolex_words.drop(emolex_words.index[0])

    emotions = emolex_words.columns.drop('word')

    stemmer = SnowballStemmer(lang)
    return stemmer, emolex_words, emotions
