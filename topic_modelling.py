import argparse
from preprocess import *
from model import *


def main(date):
	path = '/content/nytimes_news_articles.txt'
	nyTimesTemp, dates = preprocess_data('/content/nytimes_news_articles.txt')
	date_indexes = get_index_dates(date, dates)
	articles = get_articles_for_date(date_indexes, nyTimesTemp)
	run_topic_modelling(articles)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--date", help="date of articles to topic model(YYYY/MM/DD)", default='2016/05/29')
	args = parser.parse_args()


	main(args.date)

  

