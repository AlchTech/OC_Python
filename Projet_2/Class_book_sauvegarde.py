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

# FAIRE LA PAGINATION
class Books:
    def __init__(self, url_categories):
        self.url_categories = url_categories      
    def get_books(self):
        all_books = []
        for key, value in self.url_categories.items():
            dictionary_categorie_urls = {}
            list_url_products = []
            get_page = requests.get(value)
            get_soup = BeautifulSoup(get_page.content, 'html.parser') 
            for img_url in get_soup.findAll('img'):
                img_url = img_url.parent.get('href')
                img_url = "http://books.toscrape.com/catalogue/" + img_url[9:]
                list_url_products.append(img_url)
                dictionary_categorie_urls[key] = list_url_products
                
            all_books.append(dictionary_categorie_urls)
        return all_books
list_books_by_category = Books(name_url_categories).get_books()

class Book:
    
    def __init__(self, list_books_by_category):
        self.list_books_by_category = list_books_by_category

    def list_by_category(self):
        for list_books_by_category in self.list_books_by_category:
            for key, value in list_books_by_category.items():
                print(self.description_book(key, value))

    def description_book(self, name_categories, url_categories):
        for url_book in url_categories:
            get_page = requests.get(url_book)
            get_soup = BeautifulSoup(get_page.content, 'html.parser')
            # recuperation des données
            self.sent_data_csv(name_categories,  url_categories)
    

    def sent_data_csv(self, name_categories, url_categories):
            with open(name_categories + '.csv', 'w') as csvfile:
                fieldnames = ['product_page_url', 
                              'universal_product_code', 
                              'title', 'price_including_tax', 
                              'price_excluding_tax', 
                              'number_available', 
                              'product_description', 
                              'category', 
                              'review_rating', 
                              'image_url']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
    #         for list_books_by_category in self.list_books_by_category:
    #             for key, value in list_books_by_category.items():
    #                 for url in value:
    #                     get_page = requests.get(url)
    #                     get_soup = BeautifulSoup(get_page.content, 'html.parser')
    #                     get_title = get_soup.find('h1', {'class': 'title'})
    #                     get_price = get_soup.find('p', {'class': 'price_color'})
    #                     get_rating = get_soup.find('p', {'class': 'star-rating'})
    #                     get_description = get_soup.find('div', {'class': 'product_main'})
    #                     writer.writerow({'category': key, 'title': get_title.text.strip(), 'price': get_price.text.strip(), 'rating': get_rating.text.strip(), 'description': get_description.text.strip()})
                
Book(list_books_by_category).list_by_category()
# Book(list_books_by_category).descriptions_book()