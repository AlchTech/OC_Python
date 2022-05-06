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
            # if get_page_soup.findAll('li', {'class': 'next'}) != []:
            #     while get_page_soup.findAll('li', {'class': 'next'}) != []:
            #         get_next = get_page_soup.findAll('li', {'class': 'next'})[0].find('a').get('href')
            #         get_url = get_url[:-10]
            #         self.get_next = get_url  + get_next
            #         print(self.get_next)
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
                
                if not os.path.exists("images/" + key):
                    os.makedirs("images/" + key)
                
                if image_url != "http://books.toscrape.com/media/images":
                    print(image_url)
                name_image ="images/" + key + "/" + title + ".jpg"
                name_image = name_image.replace(" ", "_")
                try: 
                    urllib.request.urlretrieve(image_url, name_image)
                    if not urllib.request.urlretrieve(image_url, name_image):
                        next
                except Exception as e:
                    print(e)
                    next

                    
                    
                        
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
        
            
        # SI DOSSIER EXISTE DEJA NE FAIRE RIEN
        if  os.path.exists("./csv/" + name_category):
            os.mkdir("./csv/" + name_category)
                
        with open(name_category + '.csv', 'w', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(fieldnames)
            for row in data:
                writer.writerow(row)

        source = r'./' + name_category + '.csv'
        destination = r'./csv/' + name_category + '.csv'

        shutil.move(source,destination)
                
Book_description(name_url_book).get_description()