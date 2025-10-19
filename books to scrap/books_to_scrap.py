#importing required libiraries
import requests 
from bs4 import BeautifulSoup 
import csv
from urllib.parse import urljoin
import os
#listing all categories to use its index in link
categories = [
    'books', 'travel', 'mystery', 'historical fiction', 'sequential art', 'classics', 'philosophy', 'romance',
    'womens fiction', 'fiction', 'childrens', 'religion', 'nonfiction', 'music', 'default', 'science fiction',
    'sports and games', 'add a comment', 'fantasy', 'new adult', 'young adult', 'science', 'poetry', 'paranormal',
    'art', 'psychology', 'autobiography', 'parenting', 'adult fiction', 'humor', 'horror', 'history', 'food and drink',
    'christian fiction', 'business', 'biography', 'thriller', 'contemporary', 'spirituality', 'academic', 'self help',
    'historical', 'christian', 'suspense', 'short stories', 'novels', 'health', 'politics', 'cultural', 'erotica', 'crime'
]

books=[]

#take input from user for wanted categories
user_input=input("Enter  Categories you want books about splitted by - :  ")
categories_chosen=list(map(str.strip,user_input.split("-")))

def get_book_info(all_books, category, link):
            for i in range(len(all_books)):
                book_name = all_books[i].find('h3').find('a')['title']
                no_of_stars=all_books[i].find('p')['class'][1]
                price=all_books[i].find('div',class_="product_price").find('p').text
                Existence=all_books[i].find('p',class_="instock availability").text.strip()
                book_link=all_books[i].find('a')['href']
                books.append({"book_name":book_name,"No_of_stars":no_of_stars,"price":price,"In_stock_or_not":Existence,"Book_link":urljoin(link,book_link),"category":category})
def write_to_csv(books,category):
        file_path=r"C:\Users\samuel\Desktop\projects\python\programs\Web scraping\books to scrap\books_info.csv"
        book_headers=books[0].keys()
        file_exists = os.path.exists(file_path)
        with open(file_path, 'a', newline='', encoding="utf-8") as file:
            dict_writer=csv.DictWriter(file,book_headers)
            if not file_exists:
                dict_writer.writeheader()
            dict_writer.writerows(books)
            print(f"scraping is done for {category}")     
                  
#apply loop for each category
for category in categories_chosen:
    
    if category.lower() not in categories:
        print(f"Category '{category}' not found — skipping.")
        continue
    books=[]
    category_index=categories.index(category.lower())
    link = rf"https://books.toscrape.com/catalogue/category/books/{category.lower().replace(' ', '-')}_{category_index + 1}/index.html"
    try:
        response=requests.get(link)
        response.encoding = 'utf-8'
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error {e}")


            
    def main(response):
        soup=BeautifulSoup(response.text,'html.parser')
        all_books=soup.find_all('li',class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        get_book_info(all_books,category,link)
    
        if not books:
            print("No books found — check the category or URL.")
            return
        write_to_csv(books,category)
        
    main(response)
    
