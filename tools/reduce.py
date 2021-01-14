from glob import glob
import os


def reduce_for_letter(letter: str) -> None:
	strings = []
	with open('./letters/{}.txt'.format(letter.lower()), 'r+', encoding='utf8') as file:
		for line in file:
			strings.append(line.replace('\n', ''))

	with open('./letters/reduced/{}.txt'.format(letter.lower()), 'w+', encoding='utf8') as file:
		file.write(';'.join(strings))


def main() -> None:
	for path in glob('./letters/*.txt'):
		letter = os.path.basename(path).replace('.txt', '')
		reduce_for_letter(letter)


if __name__ == '__main__':
	main()
