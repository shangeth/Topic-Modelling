import pandas as pd
import unicodedata
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')
import re
from sklearn.decomposition import LatentDirichletAllocation
import nltk
from nltk.stem import WordNetLemmatizer
import re

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')




def process_data(path):
	print('Processing Data...')
	nyTimesFile = open(path, encoding='latin-1')
	nyTimesFile.seek(0)
	nyTimesV1 = nyTimesFile.readlines()
	nyTimesTemp = []
	nyTimesURL = []

	for i in range(0, len(nyTimesV1)-1):
	    if re.findall('URL', nyTimesV1[i]) == []:
	        sent = sent + nyTimesV1[i]
	        if (re.findall('URL', nyTimesV1[i+1]) != []) and (i+1 < len(nyTimesV1)):
	            nyTimesTemp.append(sent.strip())
	    else:
	        sent = ''
	        nyTimesURL.append(nyTimesV1[i])

	for i in range(0, len(nyTimesTemp)):
	    nyTimesTemp[i] = nyTimesTemp[i]+'articleID'+str(i)
	    
	    
	nyTimesTemp = [unicodedata.normalize('NFKD', i).encode('ascii','ignore').decode("utf-8")  for i in nyTimesTemp]
	dates = [('/').join(j.split('/')[3:6]) for j in nyTimesURL]	
	return nyTimesTemp, dates



def process_text(text):
  # lowercase
  text=text.lower()
  # word tokenize
  text = nltk.word_tokenize(text)
  # removing stop words
  stopwords = nltk.corpus.stopwords.words('english')
  text = [word for word in text if word.lower() not in stopwords]
  # lemmatization
  lemm = WordNetLemmatizer()
  text = [lemm.lemmatize(t) for t in text]
    #remove tags
  text=[re.sub("</?.*?>"," <> ",t) for t in text]
  # remove special characters and digits
  text=[re.sub("(\\d|\\W)+"," ",t) for t in text]
  text = [t for t in text if t is not ' ']
  text = " ".join(text)
  return text