import pandas as pd
import unicodedata
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')
import re
from sklearn.decomposition import LatentDirichletAllocation


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