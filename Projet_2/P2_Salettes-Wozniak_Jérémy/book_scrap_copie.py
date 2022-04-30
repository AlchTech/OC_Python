import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("http://books.toscrape.com/")    # Récupération de la page
soup = BeautifulSoup(page.content, 'html.parser')    # Parsing du code HTML


# RECUPERE URL DES CATEGORIES ET LEURS NOMS
def link_category():
    categories_url_list = []
    categories_name_list = []
    select_ul = soup.find('ul', {'class': 'nav nav-list'})
    for categorie in select_ul.find_all('a'):
        categorie_url = "http://books.toscrape.com/" + categorie.get('href')
        categorie_name = categorie.get_text().strip()
        categories_name_list.append(categorie_name)  
        categories_url_list.append(categorie_url)
    if categories_url_list[0] == 'http://books.toscrape.com/catalogue/category/books_1/index.html':
        categories_url_list.pop(0)   
    return categories_url_list
categories_url_list = link_category()


def link_product(categories_url_list):
    list_complete = []
    for categorie_url in categories_url_list:
        categorie_page = requests.get(categorie_url)
        categorie_soup = BeautifulSoup(categorie_page.content, 'html.parser')
        list_partial = []
        list_complete.append(list_partial)
        for img_url in categorie_soup.find_all('img'):
            img_url = img_url.find_parent('a', href=True)
            img_url = "http://books.toscrape.com/catalogue/" + img_url["href"][9:]
            list_partial.append(img_url)

        
    return list_complete
           

def product(link_product):
    
    # print(link_product)
    
    head = [
        "product_page_url",
        "universal_product_name", 
        "title", 
        "price_including_tax", 
        'price_excluding_tax', 
        "number_available", 
        "product_description", 
        "category", 
        "review_rating",
        "image_url"
        ]
            

    data = []
    
    for link in link_product:
        
        # RENOMMEE DATA CSV DE MANIERE DYNAMIC
            for elem in link:
                csv_page = requests.get(elem)
                csv_soup = BeautifulSoup(csv_page.content, 'html.parser')
                
                select_info = csv_soup.findAll('td')
                
                product_page_url = elem
                universal_product_name = select_info[0].get_text().strip().split('\n')
                title = csv_soup.findAll('h1')[0].get_text().strip()
                price_excluding_tax = select_info[2].get_text().strip().split('\n')
                price_including_tax = select_info[3].get_text().strip().split('\n')
                number_available = select_info[5].get_text().strip().split('\n')
                product_description = csv_soup.findAll('p')[3].get_text().strip()
                category =  csv_soup.findAll('a')[3].get_text().strip()
                review_rating = select_info[6].get_text().strip().split('\n')
                image_url = csv_soup.findAll('img')[0].get('src')
                image_url = "http://books.toscrape.com/media/" + image_url[12:]
                
                add_data = [
                    product_page_url,  
                    universal_product_name, 
                    title, 
                    price_including_tax,
                    price_excluding_tax, 
                    number_available, 
                    product_description, 
                    category, 
                    review_rating, 
                    image_url
                    ]
                data.append(add_data)
    return head, data



head, data = product(link_product(categories_url_list))  

def csv_send(head, data):
    category = "books"
    with open(category + '.csv', 'w', encoding='utf-8') as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(head)
        for elt in data:
            writer.writerow(elt)
csv_send(head, data)