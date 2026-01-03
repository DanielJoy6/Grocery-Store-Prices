"""Helper file for all Kroger stuff"""

import time
import pyautogui as pag
import pandas as pd
import pyperclip
from bs4 import BeautifulSoup

SAVE_EVERY = 10   # save every 10 items
def save_progress(products, prices, ounces, sources, prices_per_ounce, categories):    
    df = pd.DataFrame({ #Put into dataframe for saving as csv file
        'Product': products,
        'Price': prices,
        'Ounces': ounces,
        'Source': sources,
        'Price per ounce': prices_per_ounce,
        'Categories': categories
    })
    df.to_csv('Kroger Results.csv', index = False)

    print("Progress saved.")


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
            if("lb" in textarray):
                text = 16*float(textarray[0])
            else:
                text = float(textarray[0])
    return title, price, text

def kroger(foods, products, prices, ounces, sources, prices_per_ounce, categories):
    """Kroger"""
    pag.hotkey("ctrl", "l") #browser address bar
    pag.write("kroger.com", interval=0.1)
    print("Switch to Kroger.. 10 seconds")
    pag.press('enter')
    time.sleep(4)
    saved_count = 0

    for food in foods:
        pag.moveTo(1075, 300) #Search bar
        time.sleep(0.5)
        pag.click()
        time.sleep(0.5)
        pag.write(food, interval=0.1) #type in food
        pag.press('enter')
        time.sleep(8)
        pag.hotkey("ctrl", "shift", "c")   # Open devtools
        time.sleep(1)
        pag.hotkey("ctrl", "shift", "k")   # Console
        time.sleep(1)
        pag.write("copy(document.body.innerHTML)")
        time.sleep(0.5)
        pag.press("enter")
        time.sleep(1)
        html = pyperclip.paste()
        soup = BeautifulSoup(html, "html.parser") #Pass into beautiful soup
        product_titles = soup.select('span[data-testid="cart-page-item-description"]')
        price_tags = soup.select('data.kds-Price--alternate')
        temp_ounces = soup.select('span[data-testid="product-item-sizing"]')
        print("Found", len(product_titles), "product titles")
        if(len(product_titles) == 0):
            pag.write("copy(document.body.innerHTML)")
            time.sleep(0.5)
            pag.press("enter")
            time.sleep(1)
            html = pyperclip.paste()
            soup = BeautifulSoup(html, "html.parser") #Pass into beautiful soup
            product_titles = soup.select('span[data-testid="cart-page-item-description"]')
            price_tags = soup.select('data.kds-Price--alternate')
            temp_ounces = soup.select('span[data-testid="product-item-sizing"]')
            time.sleep(0.1)
            print("Retrying found", len(product_titles), "product titles")
        counter = 0
        for product, ounce, price in zip(product_titles, temp_ounces, price_tags):
            product, price, ounce = find_ounces_kroger(
                product.get_text(strip=True),
                price["value"],
                ounce.get_text(strip=True)
            )

            print(product, ": ", price)

            products.append(product)
            prices.append(price)
            ounces.append(ounce)

            try:
                prices_per_ounce.append(float(price)/float(ounce))
            except ValueError:
                prices_per_ounce.append(0)

            categories.append(foods.index(food))
            sources.append("Kroger")

            counter += 1
            if counter > 5:
                break
        saved_count += 1
        if saved_count % SAVE_EVERY == 0:
            save_progress(products, prices, ounces, sources, prices_per_ounce, categories)

        pag.hotkey("ctrl", "shift", "i") #Close out source code
        time.sleep(0.2)
        
        pag.moveTo(1542, 293) #Search bar
        pag.click()
        time.sleep(1)
    # Final save for leftovers
    if products:
        save_progress(products, prices, ounces, sources, prices_per_ounce, categories)

