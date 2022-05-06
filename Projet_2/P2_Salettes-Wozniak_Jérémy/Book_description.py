from webbrowser import get
import requests
from bs4 import BeautifulSoup
import csv

class Categories:
    def __init__(self, url):
        self.url = url     
    def get_categories(self):
        categories = {}
        get_page = requests.get(self.url)
        get_soup = BeautifulSoup(get_page.content, 'html.parser')
        get_categories = get_soup.find('ul', {'class': 'nav nav-list'})
        for a in get_categories.find_all('a'):
            categories_url = self.url + a.get('href')
            categories_name = a.string.strip()
            categories[categories_name] = categories_url
        return categories
name_url_categories = Categories("http://books.toscrape.com/").get_categories()


class Books:
    def __init__(self, url_categories):
        self.dictionary_categorie = url_categories

        
        
    def get_books(self):
        increment = 0
        dictionary_books = {}
        if "Books" in self.dictionary_categorie.keys():
            del self.dictionary_categorie["Books"]
            
        for key, value in self.dictionary_categorie.items():
            list_books_by_category = []
            get_name = key
            get_url = value
            get_page = requests.get(get_url) or requests.get(self.get_next)
            get_page_soup = BeautifulSoup(get_page.content, 'html.parser')
            get_url_book = get_page_soup.findAll('h3')
            increment += 1
            for book in get_url_book:
                books_url = book.find('a').get('href')
                if books_url.startswith('../../'):
                    books_url = books_url[6:]
                if books_url.startswith('../'):
                    books_url = books_url[3:]
                books_url = "http://books.toscrape.com/catalogue/" + books_url
                list_books_by_category.append(books_url)
            dictionary_books[get_name] = list_books_by_category

            # PAGINATION
            if get_page_soup.findAll('li', {'class': 'next'}) != []:
                while get_page_soup.findAll('li', {'class': 'next'}) != []:
                    get_next = get_page_soup.findAll('li', {'class': 'next'})[0].find('a').get('href')
                    get_url = get_url[:-10]
                    self.get_next = get_url  + get_next
                    print(self.get_next)
        return dictionary_books                
            
name_url_book = Books(name_url_categories).get_books()
print(name_url_book)