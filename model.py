import pandas as pd
import unicodedata
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')
import re
from sklearn.decomposition import LatentDirichletAllocation



def get_index_dates(date, dates):
	indexes = [i for i,x in enumerate(dates) if x == date]
	return indexes

def get_articles_for_date(date_indexes, nyTimesTemp):
	arti = np.array(nyTimesTemp)
	arti = list(arti[date_indexes])
	return arti



class LemmaCountVectorizer(CountVectorizer):
	def build_analyzer(self):
		lemm = WordNetLemmatizer()
		analyzer = super(LemmaCountVectorizer, self).build_analyzer()
		return lambda doc: (lemm.lemmatize(w) for w in analyzer(doc))

def print_top_words(model, feature_names, n_top_words):
    for index, topic in enumerate(model.components_):
        message = "Words making the topics in article : "
        message += " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1 :-1]])
        print(message,'\n')
        # print("="*70)
        
        
        
      
def run_topic_modelling(X):
	text = [X]
	# print(text)
	tf_vectorizer = LemmaCountVectorizer(max_df=1, 
	                                   min_df=0,
	                                   stop_words='english',
	                                   decode_error='ignore')
	tf = tf_vectorizer.fit_transform(text)
	lda = LatentDirichletAllocation(n_components=1, max_iter=20,
	                            learning_method = 'batch',
	                            learning_offset = 50.,
	                            random_state = 0)
	lda.fit(tf)
	n_top_words = 10
	tf_feature_names = tf_vectorizer.get_feature_names()
	print_top_words(lda, tf_feature_names, n_top_words)