import sys
import os


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
	if len(sys.argv) < 2:
		error('No input word')
	
	word = sys.argv[1].lower()

	finded = find_strict(word)
	if not finded:
		error('Not finded')


if __name__ == '__main__':
	main()