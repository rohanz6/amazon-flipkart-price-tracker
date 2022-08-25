from http import server
from itertools import product
import requests
from bs4 import BeautifulSoup
import smtplib
import time



URL = "https://www.amazon.in/Apple-iPhone-13-Pro-128GB/dp/B09G99YPQM/ref=sr_1_2_sspa?keywords=iphone+13&qid=1661448771&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUElOVkE5NkdWM1RWJmVuY3J5cHRlZElkPUEwOTM4NDg3VURaSVdET04ySldLJmVuY3J5cHRlZEFkSWQ9QTA4NzQ0ODgxUzhGVUg2TkdKV0FDJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

#this will just give us some basic information of our browser 
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'}

email_address = ""
password = ""
to_address = ""



def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find('span', {"class" : "a-price-whole"}).get_text()


    product_price = ''
    for letter in price:
        if letter.isnumeric():
            product_price += letter
        
    product_price = float(product_price)

    if product_price > 104000:
        send_mail()
    
    

    print(title.strip())
    print(product_price)

def send_mail():
    # establising a connection b/n our connection & gmails connections
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls() # encrypty our connection
    server.ehlo()

    server.login(email_address, password)
    subject = 'Price fell down'
    body = 'https://www.amazon.in/Apple-iPhone-13-Pro-128GB/dp/B09G99YPQM/ref=sr_1_2_sspa?keywords=iphone+13&qid=1661448771&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUElOVkE5NkdWM1RWJmVuY3J5cHRlZElkPUEwOTM4NDg3VURaSVdET04ySldLJmVuY3J5cHRlZEFkSWQ9QTA4NzQ0ODgxUzhGVUg2TkdKV0FDJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        email_address,
        to_address,
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

    

while True:
    check_price()
    time.sleep(60)