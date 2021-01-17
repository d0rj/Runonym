import sys
import os


def error(message: str) -> None:
	print('--', message, '--')
	exit(1)


def main() -> None:
	if len(sys.argv) < 2:
		error('No input word')
	
	word = sys.argv[1].lower()

	filepath = './letters/{}.txt'.format(word[0])
	if not os.path.exists(filepath):
		error('No such synonyms')

	with open(filepath, 'r+', encoding='utf8') as file:
		for string in file:
			if string.lower().startswith(word):
				result = string.lower().replace('{},'.format(word), '')
				print(result)
				return

	error('Not finded')


if __name__ == '__main__':
	main()