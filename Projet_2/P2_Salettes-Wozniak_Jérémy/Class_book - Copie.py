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
                self.description_book(key, value)

    def description_book(self, name_categories, url_categories):
        
        for url_book in url_categories:
            get_page = requests.get(url_book)
            get_soup = BeautifulSoup(get_page.content, 'html.parser')
            select_info = get_soup.findAll('td')
            send_data = []
            
            
            if select_info == [] or select_info == None:
                print("No data")
            else:
                
                # DATA 
                product_page_url = url_book
                # universal_product_code= select_info[0].get_text().strip()
                # title = get_soup.findAll('h1')[0].get_text().strip()
                # price_excluding_tax = select_info[2].get_text().strip().split('\n')
                # price_including_tax = select_info[3].get_text().strip().split('\n')
                # number_available = select_info[5].get_text().strip().split('\n')
                # product_description = get_soup.findAll('p')[3].get_text().strip()
                # category =  get_soup.findAll('a')[3].get_text().strip()
                # review_rating = select_info[6].get_text().strip().split('\n')
                # image_url = get_soup.findAll('img')[0].get('src')
                # image_url = "http://books.toscrape.com/media/" + image_url[12:]

                data = [
                    product_page_url,
                    # universal_product_code,
                    # title,
                    # price_including_tax,
                    # price_excluding_tax,
                    # number_available,
                    # product_description,
                    # category,
                    # review_rating,
                    # image_url,
                ]
                
                send_data(data)
                
                self.sent_data_csv(name_categories,  send_data)
    

    def sent_data_csv(self, name_categories, data):
            with open(name_categories + '.csv', 'w') as csvfile:
                fieldnames = ['product_page_url', 
                              'universal_product_code', 
                              'title', 
                              'price_including_tax', 
                              'price_excluding_tax', 
                              'number_available', 
                              'product_description', 
                              'category', 
                              'review_rating', 
                              'image_url']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for element in data:
                    writer.writerow(element)
                

Book(list_books_by_category).list_by_category()
# Book(list_books_by_category).descriptions_book()