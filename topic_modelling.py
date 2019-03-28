import argparse
from preprocess import *
from model import *
from get_articles import *


def main(date):
	path = '/content/nytimes_news_articles.txt'
	# nyTimesTemp, dates = process_data('./data/nytimes_news_articles.txt') #for file
	nyTimesTemp, nyTimesTitle = get_articles(date) # for API
	# date_indexes = get_index_dates(date, dates) #for file
	# articles = get_articles_for_date(date_indexes, nyTimesTemp) #for file

	articles = nyTimesTemp # for API
	articles = [process_text(i) for i in articles]
	for i in range(len(articles)):
		print('Running Topic Modelling on Article : {}'.format(nyTimesTitle[i]))
		run_topic_modelling(articles[i])


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--date", help="date of articles to topic model(YYYY/MM/DD)", default='2016/05/29')
	args = parser.parse_args()


	main(args.date)

  

