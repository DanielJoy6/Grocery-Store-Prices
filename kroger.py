"""Helper file for all Kroger stuff"""

import time
import pyautogui as pag
import pyperclip
from bs4 import BeautifulSoup

def find_ounces_kroger(title, price, text):
    """Fixes Kroger's tendency to fix amount and price/amount in same field"""
    if "Â®" in title: #Remove the Registered symbol from product titles
        title = title[:title.index("Â®")] + title[title.index("Â®")+2:]

    if "$" in text: #If it grabbed price per amount instead of amount
        number = float(text[1:text.index("/")])
        try:
            text = float(price)/number
        except ValueError:
            text = 0
    else: #It grabbed ounces correctly
        textarray = text.split()
        if("oz" in textarray or "fl oz" in textarray or "lb" in textarray):
            text = float(textarray[0])
    return title, price, text

def kroger(foods, products, prices, ounces, sources, prices_per_ounce, categories):
    """Kroger"""
    pag.hotkey("ctrl", "l") #browser address bar
    pag.write("kroger.com", interval=0.1)
    print("Switch to Kroger.. 10 seconds")
    time.sleep(3)
    for food in foods:
        pag.moveTo(1160, 173) #Search bar
        time.sleep(0.5)
        pag.click()
        time.sleep(0.5)
        pag.write(food, interval=0.1) #type in food
        pag.press('enter')
        time.sleep(6)
        pag.hotkey("ctrl", "u") #Open up source code
        time.sleep(3)
        pag.hotkey("ctrl", "a") #Copy it all
        time.sleep(0.3)
        pag.hotkey("ctrl", "c")
        time.sleep(1.5)
        html = pyperclip.paste()
        soup = BeautifulSoup(html, "html.parser") #Pass into beautiful soup
        product_titles = soup.find_all("span", {"data-testid": "cart-page-item-description"})
        time.sleep(0.1)
        temp_ounces = soup.find_all("span", {"class": "kds-Text--s text-neutral-more-prominent"})
        time.sleep(0.1)
        price_tags = soup.find_all("data", {"class": "kds-Price kds-Price--alternate"})
        time.sleep(0.1)
        print("Found", len(product_titles), "product titles")
        counter = 0
        for product, ounce, price in zip(product_titles, temp_ounces, price_tags):
            product, price, ounce = find_ounces_kroger(product.get_text(strip=True),
                    price["value"], ounce.get_text(strip=True)) #Get text in good format
            print(product, ": ", price)
            products.append(product)
            prices.append(price)
            ounces.append(ounce)
            try: #Sometimes fails
                prices_per_ounce.append(float(price)/float(ounce))
            except ValueError:
                prices_per_ounce.append(0)
            categories.append(foods.index(food))
            sources.append("Kroger")
            counter += 1
            if counter > 5:
                break #
        pag.hotkey("ctrl", "w") #Close out source code
        time.sleep(0.2)
        pag.moveTo(1552, 169) #Move back to search bar
        pag.click()
        time.sleep(1)
