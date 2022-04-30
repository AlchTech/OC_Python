import requests
from bs4 import BeautifulSoup
import csv

class get_categories:

    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.category = ''
        self.select_ul = self.soup.find('ul', {'class': 'nav nav-list'})

    def get_categories(self):
        dict_categories = {}
        
        for category in self.select_ul.find_all('a'):
            category_url = "http://books.toscrape.com/" + category.get('href')
            category_name = category.get_text().strip()
            dict_categories[category_name] = category_url
        if dict_categories['Books'] == 'http://books.toscrape.com/catalogue/category/books_1/index.html':
            del dict_categories['Books']
        return dict_categories
categorie_toscrape = get_categories("http://books.toscrape.com/")

class get_products:
    
    def __init__(self, dict_categories):
        # self.url_product_category = []
        self.dict_categories = dict_categories
        print(dict_categories)
        self.key
        self.value
        
    def url_product_category(self, dict_categories):
        self.dict_categories = dict_categories

        for key, value in dict.items():
            self.key = key
            self.value = value
            
            
        # for key, value in dict.items():
        #     self.key = key              
        #     self.value = value
        #     self.page = requests.get(self.value)
        #     self.soup = BeautifulSoup(self.page.content, 'html.parser')

            # AJOUTER UNE LISTE D'URL POUR CHAQUE CATEGORIE
            # return self.sent_dict_products()
            # url_product_by_categories = self.sent_dict_products()
            # self.url_product_category.append(url_product_by_categories)
        # print(self.url_product_category)
    
    # def url_for_products(self):
    #     print(self.soup.find_all('img'))
    #     list_url_product = []
    #     for img_url in self.soup.find_all('img'):
    #         img_url = img_url.find_parent('a', href=True)
    #         img_url = "http://books.toscrape.com/catalogue/" + img_url["href"][9:]
    #         list_url_product.append(img_url) 
        # print(list_url_product)
    

    # def sent_dict_products(self):
    #     self.dict_products = {}
    #     key_url = self.url_for_products()
    #     self.dict_products[self.key] = key_url
    #     print(self.dict_products)     
    
get_products(categorie_toscrape.get_categories())
# dict_products = get_products(categorie_toscrape.get_categories()).url_for_products()
# dict_products = get_products(categorie_toscrape.get_categories()).sent_dict_products()
# print(dict_products)

# class book:
#     def __init__(self, dict)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     def __init__(self, url):
#         self.url = url
#         self.page = requests.get(self.url)
#         self.soup = BeautifulSoup(self.page.content, 'html.parser')
#         self.select_info = self.soup.findAll('td')
        
#     def get_data(self):
#         dict_data = {}
#         dict_data['product_page_url'] = self.url
#         dict_data['universal_product_name'] = self.select_info[0].get_text().strip().split('\n')
#         dict_data['title'] = self.soup.findAll('h1')[0].get_text().strip()
#         dict_data['price_including_tax'] = self.select_info[2].get_text().strip().split('\n')
#         dict_data['price_excluding_tax'] = self.select_info[3].get_text().strip().split('\n')
#         dict_data['number_available'] = self.select_info[4].get_text().strip().split('\n')
#         dict_data['product_description'] = self.soup.findAll('p')[0].get_text().strip()
#         dict_data['category'] = self.soup.findAll('a')[0].get_text().strip()
#         dict_data['review_rating'] = self.soup.findAll('span')[0].get_text().strip()
#         dict_data['image_url'] = self.select_img['src']
#         return dict_data


# class get_csv_data:
    
#     def __init__(self, dict):
#         self.dict = dict
#         self.dict_data = get_data(self.dict['product_page_url']).get_data()
        
#     def get_csv_data(self):
#         with open('books.csv', 'a') as csv_file:
#             writer = csv.writer(csv_file)
#             writer.writerow(self.dict_data.values())










# class categories:
#     page = requests.get("http://books.toscrape.com/")    # Récupération de la page
#     soup = BeautifulSoup(page.content, 'html.parser')    # Parsing du code HTML
#     select_ul = soup.find('ul', {'class': 'nav nav-list'})

    
#     def __init__(self):
#         self.name = self.categories_name_list = []
#         self.url = self.categories_url_list = []
#         self.list_complete = []
        

        
#     def link_category(self):
#         for categorie in self.select_ul.find_all('a'):
#             self.categorie_url = "http://books.toscrape.com/" + categorie.get('href')
#             self.categories_url_list.append(self.categorie_url)
#         if self.categories_url_list[0] == 'http://books.toscrape.com/catalogue/category/books_1/index.html':
#             self.categories_url_list.pop(0)
#         return self.categories_url_list
    
#     def section_category(self):
#         for self.url, self.name in zip(self.categories_url_list, self.categories_name_list):
#             self.list_complete.append([self.url, self.name])
#         return self.list_complete

        
# categories1 = categories()
# categories1.name_category()
# categories1.link_category()
# list_category = categories1.section_category()

# class page_categories:
    
#     def __init__(self, list_category):
#         self.name = self.categories_name_list = []
#         self.url = self.categories_url_list = []
        

#     def link_product(self):
#         print(self.name)
    
# theme = page_categories
# theme = theme.link_product(list_category)

# print(theme)
# # class page_books:
# #     def __init__(self, name, url):
# #         self.name = name
# #         self.url = url
        
# # class book:
# #     def __init__(self, name, url):
# #         self.name = name
# #         self.url = url
        
# # class book_csv:
# #     def __init__(self, name, url):
# #         self.name = name
# #         self.url = url