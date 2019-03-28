from nytimesarticle import articleAPI
import requests
import json
from newsplease import NewsPlease



def get_articles(date):
	articles_urls = []
	articles_texts = []
	articles_titles = []
	date = int("".join(date.split('/')))
	try:
		api = articleAPI('Kj8eaq15hll4dUHoGW2NdAi3cwhJ20Ol')
	except: 
		print('Error in API key or API connection!!')

	articles = api.search(begin_date = date)

	if articles['status'] == 'OK':
		# print(articles['response']['docs'][0].keys())

		articles = articles['response']['docs']
		for article in articles:
			articles_urls.append(article['web_url'])
	else: 
		print('Date Not found !!')

	for url in articles_urls:	
		article = NewsPlease.from_url(url)
		articles_texts.append(article.text)
		articles_titles.append(article.title)

	return articles_texts, articles_titles

def main():
	get_articles('2019/03/28')


if __name__ == '__main__':
	main()