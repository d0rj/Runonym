import requests
from bs4 import BeautifulSoup
from typing import Dict, List


RUSSIAN_ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщыэюя'.split()

BASE_URL = 'https://text.ru'
TEXT_RU_URL = BASE_URL + '/synonym'
LETTER_URL = lambda letter, from_count: \
				TEXT_RU_URL + '/letter/{0}/{1}'.format(letter, from_count)

SYNS_PER_PAGE = 300


def create_urls_for_letter(letter: str) -> List[str]:
	page = requests.get(TEXT_RU_URL)
	soup = BeautifulSoup(page.text, 'lxml')

	letters_finded = soup.find_all('span', { 'class': 'syn-first-letter' })
	right_letter = [lf for lf in letters_finded if (lf.findChild().findChild().text).lower() == letter][0]

	syn_count = str(right_letter.find('span', { 'class': 'counter' }, recursive=False).text)
	syn_count = int(syn_count.replace('[', '').replace(']', ''))

	result = []
	count = 0
	needed_url = lambda from_count: LETTER_URL(letter, from_count)
	while count < syn_count:
		result.append(needed_url(count))
		count += SYNS_PER_PAGE

	return result


def word_syns_from_url(url: str) -> List[str]:
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'lxml')

	elements = soup.find_all('td', { 'class': 'ta-l' })
	result = [str(el.findChild().text) for el in elements]
	return result


def get_for_letter(letter: str) -> Dict[str, List[str]]:
	letter_urls = create_urls_for_letter(letter)

	result = {}
	for letter_url in letter_urls:
		page = requests.get(letter_url)
		soup = BeautifulSoup(page.text, 'lxml')

		words_elements = soup.find_all('div', { 'class': 'ellipsis' })
		for word_element in words_elements:
			href = BASE_URL + str(word_element.findChild().get('href'))
			word = str(word_element.findChild().text)

			result[word] = word_syns_from_url(href)

	return result



def main():
	synonyms = get_for_letter('ж')

	with open('Буква Ж.txt', 'w', encoding='utf8') as file:
		for word in synonyms:
			file.write(word)
			file.write(',')
			file.write(str(synonyms[word]))
			file.write('\n')


if __name__ == '__main__':
	main()
