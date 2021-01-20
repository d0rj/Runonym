import sys
import os
import argparse
from typing import Callable


PROGRAMM_VERSION = '0.1'


def error(message: str) -> None:
	print('--', message, '--')
	exit(1)


def find_strict(word: str) -> bool:
	"""
	Searches synonym for given word literally
	"""

	filepath = './letters/{}.txt'.format(word[0])

	if not os.path.exists(filepath):
		error('No such synonyms')

	with open(filepath, 'r+', encoding='utf8') as file:
		for string in file:	
			if string.lower().startswith(word):
				result = string.lower().replace('{},'.format(word), '')
				print(result)
				return True

	return False


def find_started(word: str) -> bool:
	"""
	Searches synonyms for all words started with given but lemmatized
	"""

	from nltk.stem.snowball import SnowballStemmer 

	filepath = './letters/{}.txt'.format(word[0])

	if not os.path.exists(filepath):
		error('No such synonyms')

	stemmer = SnowballStemmer("russian") 
	stemmed_word = stemmer.stem(word)

	finded = False
	with open(filepath, 'r+', encoding='utf8') as file:
		for string in file:	
			if string.lower().startswith(stemmed_word):
				result = string.lower().replace('{},'.format(word), '')
				print(result)
				finded = True

	return finded


def main() -> None:
	parser = argparse.ArgumentParser('runonym', description='Simple programm to search synonym for russian words.')
	parser.add_argument('-w', '--word', action='store', type=str, required=True, help='Word to search')
	parser.add_argument('--starts', action='store_true', help='Flag: Search synonyms for all words starts with given word but lemmatized.')
	parser.add_argument('-v', '--version', action='version', version='Runonym {}'.format(PROGRAMM_VERSION))

	parsed_args = parser.parse_args(sys.argv[1:])
	
	word = str(parsed_args.word).lower()

	search_function: Callable[[str], bool]
	if bool(parsed_args.starts):
		search_function = find_started
	else:
		search_function = find_strict

	finded = search_function(word)
	if not finded:
		error('Not finded')


if __name__ == '__main__':
	main()