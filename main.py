import sys
import os
from nltk.stem.snowball import SnowballStemmer 


def error(message: str) -> None:
	print('--', message, '--')
	exit(1)


def main() -> None:
	stemmer = SnowballStemmer("russian") 

	if len(sys.argv) < 2:
		error('No input word')
	
	word = sys.argv[1].lower()
	stemmed_word = stemmer.stem(word)

	filepath = './letters/{}.txt'.format(word[0])
	if not os.path.exists(filepath):
		error('No such synonyms')

	finded = False
	with open(filepath, 'r+', encoding='utf8') as file:
		for string in file:	
			if string.lower().startswith(stemmed_word):
				result = string.lower().replace('{},'.format(word), '')
				print(result)
				finded = True

	if not finded:
		error('Not finded')


if __name__ == '__main__':
	main()