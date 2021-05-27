import hashlib
import json

WIKI_LINK = 'https://en.wikipedia.org/wiki/'
INITIAL_FILE = 'countries.json'
FINAL_FILE = 'result.txt'


class Wikipedia:

    def __init__(self, file_path):
        with open(file_path) as f:
            all_data = json.load(f)
            country_titles = (country['name']['common'] for country in all_data)
            self.country_titles_iter = iter(country_titles)

    def get_link(self, country_title: str):
        country_title = country_title.replace(' ', '_')
        country_wiki_url = f'{WIKI_LINK}{country_title}'
        return country_wiki_url

    def __iter__(self):
        return self

    def __next__(self):
        country_title = next(self.country_titles_iter)
        final_link = f'{country_title} - {self.get_link(country_title)}'
        return final_link


def get_hash(path: str):
    with open(path) as f:
        for item in f:
            yield hashlib.md5(item.encode()).hexdigest()


if __name__ == '__main__':
    with open(FINAL_FILE, 'w', encoding='utf-8') as f:
        for country_link in Wikipedia(INITIAL_FILE):
            f.write(f'{country_link}\n')

for hash_list in get_hash(FINAL_FILE):
    print(hash_list)
