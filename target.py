"""Helper file for all Target Stuff"""
import time
import pyautogui as pag
import pyperclip
from bs4 import BeautifulSoup

def find_ounces(product_title):
    """Find ounces using product title when not explicitly given"""
    total = 0
    product_title = product_title.lower()
    temparray = product_title.split() #Split title into separate words
    if "oz" in temparray:
        if temparray[temparray.index("oz")-1] == "fl": #If in fl oz
            total = temparray[temparray.index("fl")-1]
        else: #if just in oz
            total = temparray[temparray.index("oz")-1]
    elif "lb" in temparray:
        total = 16*int(temparray[temparray.index("lb")-1])
    elif "gl" in temparray:
        total = 128*int(temparray[temparray.index("lb")-1])
    else:
        for item in temparray:
            if "lb" in item:
                try:
                    total = int(item[:item.index("lb")])
                except ValueError:
                    total = 0
        total = 0
    return total

def target(foods, products, prices, ounces, sources, prices_per_ounce, categories):
    """Target"""
    pag.hotkey("ctrl", "l") #browser address bar
    pag.write("target.com", interval=0.1)
    pag.press('enter')
    time.sleep(4)
    print("Switching to Target.. 5 seconds")
    pag.hotkey("ctrl", "shift", "i") #Open inspect
    time.sleep(4)
    for food in foods:
        pag.moveTo(384, 302) #Search bar
        time.sleep(0.5)
        pag.click()
        time.sleep(0.5)
        pag.hotkey("ctrl", "a")
        time.sleep(0.2)
        pag.press("delete")
        time.sleep(0.1)
        pag.write(food, interval=0.1) #type in food
        pag.press('enter')
        time.sleep(4)
        pag.moveTo(1156, 250)
        time.sleep(0.5)
        pag.click()
        time.sleep(0.1)
        pag.hotkey("ctrl", "c")
        time.sleep(1)
        html = pyperclip.paste()
        soup = BeautifulSoup(html, "html.parser") #Pass into BeautifulSoup
        product_titles = soup.find_all("div", {"class": "styles_ndsTruncate__0rtO0"})
        temp_prices = []
        prices_elements = soup.find_all("span", {"data-test": "current-price"})
        print("Found", len(prices_elements), "price containers and", len(product_titles), "product titles")
        if product_titles:
            first_title = product_titles[0].get_text(strip=True).lower()
            if "knoxville" in first_title:
                product_titles = product_titles[1:]
        for element in prices_elements:
            try:
                price = element.get_text(strip=True)
                price = price.split('$')[-1]
                temp_prices.append(float(price))
            except ValueError:
                print("Error fetching price")
                temp_prices.append(0.0)

        counter = 0
        for product, price in zip(product_titles, temp_prices):
            products.append(product.get_text(strip=True))
            prices.append(price)
            ounces.append(find_ounces(product.get_text(strip=True)))
            prices_per_ounce.append(0)
            categories.append(foods.index(food))
            sources.append("Target")
            counter += 1
            if counter > 5:
                break #
        #pag.hotkey("ctrl", "w")
        #time.sleep(0.2)
