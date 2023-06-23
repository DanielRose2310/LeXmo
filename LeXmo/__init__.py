import requests
from io import StringIO
import os
from LeXmo.settings import api,lexicon,lex_dir

if not os.path.exists(f'{lex_dir}{lexicon}'):
    print("Local lexicon data not found, downloading...")
    try:
        response = requests.get(f'{api}{lexicon}')
    except Exception as e:
        print("Can't access lexicon data.")
    if response:
        nrc = response.text
        f = open(f'{lex_dir}{lexicon}','w')
        f.write(nrc)