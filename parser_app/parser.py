import urllib.request
from bs4 import BeautifulSoup


class Parser:
    category_div_class = 'Ktdaqe'
    category_name_class = 'sv0AUd bs3Xnd'
    game_name_div_class = 'WsMG1c nnK0zc'

    def __init__(self, url: str):
        self.url = url

    def get_parsed_objects(self):
        get = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(get.read())
        return self.pars_names_and_categories(soup)

    def pars_names_and_categories(self, soup: BeautifulSoup):
        """ Pars html to find game category and game names """
        res = []
        categories = soup.find_all('div', class_=self.category_div_class)
        for cat in categories:
            category_name = cat.find('h2', class_=self.category_name_class).string
            game_names = cat.find_all('div', class_=self.game_name_div_class)
            for name in game_names:
                res.append((category_name, name.string))
        return res

    @classmethod
    def filter_by_substring(cls, substring, parsed_data):
        return [obj for obj in parsed_data if substring in obj[1]]


class FormattedPrint:

    def __init__(self, objects):
        self.objects = objects

    @staticmethod
    def formatter(objects):
        formatted_objects = ''.join([f'<li>{obj[0]}/{obj[1]}</li>' for obj in objects])
        return f'<ul>{formatted_objects}</ul>'

    def print_with_format(self):
        objects = self.formatter(self.objects)
        for obj in objects:
            print(obj)
