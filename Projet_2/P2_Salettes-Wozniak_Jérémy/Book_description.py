from base64 import encode
import os
from pydoc import describe
import shutil
from webbrowser import get
import requests
from bs4 import BeautifulSoup
import csv
import urllib.request

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

    
    def pagination(self):
        new_dictionary = {}
        for key, value in self.dictionary_categorie.items():
            if key == 'Books':
                print("Ignore la categorie Books")
            else:
                url_tmp = []
                url_tmp.append(value)
                for url in url_tmp:
                    get_next_page = requests.get(url)
                    get_soup_page = BeautifulSoup(get_next_page.content, 'html.parser')
                    if get_soup_page.findAll('li', {'class': 'next'}) != []:
                        next = get_soup_page.findAll('li', {'class': 'next'})[0].find('a').get('href')
                        next = value.replace("index.html", next)
                        url_tmp.append(next)
                        
                new_dictionary[key] = url_tmp
        return new_dictionary

        
    def get_books(self):
        pagination = self.pagination()
        dictionary_books = {}
        for key, value in pagination.items():
            for page in value:
                list_books_by_category = []
                get_page = requests.get(page)
                get_soup = BeautifulSoup(get_page.content, 'html.parser')
                get_url_book = get_soup.findAll('h3')
                for a in get_url_book:
                    a = a.find('a').get('href')
                    if a.startswith('../../'):
                        a = a[6:]
                    if a.startswith('../'):
                        a = a[3:]
                    a =  "http://books.toscrape.com/catalogue/" + a
                    list_books_by_category.append(a)
                dictionary_books[key] = list_books_by_category
                
        return dictionary_books          
            
name_url_book = Books(name_url_categories).get_books()


class Book_description:
    
    def __init__(self, url_book):
        self.url_book = url_book

    def get_description(self):
        for key, value in self.url_book.items():
            list_description = []
            for book in value:
                get_page = requests.get(book)
                get_soup = BeautifulSoup(get_page.content, 'html.parser')
                select_info = get_soup.findAll('td')
                
                product_page_url = book
                universal_product_code= select_info[0].get_text().strip()
                title = get_soup.findAll('h1')[0].get_text().strip()
                price_excluding_tax = select_info[2].get_text().strip().split('\n')
                price_including_tax = select_info[3].get_text().strip().split('\n')
                number_available = select_info[5].get_text().strip().split('\n')
                product_description = get_soup.findAll('p')[3].get_text().strip()
                category =  get_soup.findAll('a')[3].get_text().strip()
                review_rating = select_info[6].get_text().strip().split('\n')
                image_url = get_soup.findAll('img')[0].get('src')
                image_url = "http://books.toscrape.com/media/" + image_url[12:]
                print(image_url)
                
                data = [
                    product_page_url,
                    universal_product_code,
                    title,
                    price_including_tax,
                    price_excluding_tax,
                    number_available,
                    product_description,
                    category,
                    review_rating,
                    image_url,
                    ]
                
                
                os.makedirs('./images/' + key, exist_ok=True)
                urllib.request.urlretrieve(image_url, "./images/" + image_url[-12:])
                shutil.move("./images/" + image_url[-12:], "./images/" + key)
                # name_image = key + "_" + title + ".jpg"
                # urllib.request.urlretrieve(image_url, name_image)
                # # SI name_image ne contient pas .jpg print(image_url)
                # if name_image.endswith(".jpg"):
                #     print(image_url)
                # shutil.move(name_image, './images/') 
                    
                    
                    
                list_description.append(data)
            self.description_csv(key, list_description)

        

      
                
            
    def description_csv(self, name_category, data):
        fieldnames = [
            'product_page_url',
            'universal_product_code',
            'title',
            'price_including_tax',
            'price_excluding_tax',
            'number_available', 
            'product_description', 
            'category', 
            'review_rating', 
            'image_url'
            ]

        with open(name_category + '.csv', 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(fieldnames)
            for row in data:
                writer.writerow(row)
        
            
        os.makedirs("./csv/" + name_category, exist_ok=False)
        source = r'./' + name_category + '.csv'
        destination = r'./csv/' + name_category
        shutil.move(source,destination)
                
Book_description(name_url_book).get_description()
