import argparse
from preprocess import *
from model import *


def main(date):

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--date", help="date of articles to topic model(YYYY/MM/DD)", default='2016/05/29')
	args = parser.parse_args()


	main(args.date)

  

