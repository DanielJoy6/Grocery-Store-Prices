"""Helper file for all Walmart Stuff"""
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


def walmart(foods, products, prices, ounces, sources, prices_per_ounce, categories):
    """Walmart"""
    pag.hotkey("ctrl", "l") #browser address bar
    pag.write("walmart.com", interval=0.1)
    pag.press('enter')
    time.sleep(4)
    print("Switch to Walmart.. 5 seconds")
    time.sleep(5)
    for food in foods:
        pag.moveTo(1381, 165) #Search bar
        time.sleep(0.5)
        pag.click()
        time.sleep(0.5)
        pag.write(food, interval=0.1) #type in food
        pag.press('enter')
        time.sleep(5)
        pag.hotkey("ctrl", "r") #Refresh since it messes up sometimes
        time.sleep(5)
        pag.hotkey("ctrl", "u") #Open source code
        time.sleep(4)
        pag.hotkey("ctrl", "a")
        time.sleep(0.2)
        pag.hotkey("ctrl", "c")
        time.sleep(1)
        html = pyperclip.paste()
        soup = BeautifulSoup(html, "html.parser") #Pass into BeautifulSoup
        product_titles = soup.find_all("span", {"data-automation-id": "product-title"})
        #price_per_ounce = soup.find_all("div", {"data-testid": "product-price-per-unit"})
        temp_prices = []
        price_containers = soup.find_all("div", {"data-automation-id": "product-price"})
        print("Found", len(price_containers), "price containers")
        for container in price_containers:
            price_span = container.find("span", {"class": "w_iUH7"})
            if price_span:
                try:
                    price = price_span.get_text(strip=True)
                    price = price.split('$')[-1]
                    temp_prices.append(float(price))
                except ValueError:
                    print("Error fetching price")
                    temp_prices.append(0.0)
            else:
                temp_prices.append(0.0)

        counter = 0
        for product, price in zip(product_titles, temp_prices):
            print(product.get_text(strip=True), ": ", price)
            products.append(product.get_text(strip=True))
            prices.append(price)
            ounces.append(find_ounces(product.get_text(strip=True)))
            prices_per_ounce.append(0)
            categories.append(foods.index(food))
            sources.append("Walmart")
            counter += 1
            if counter > 5:
                break #
        pag.hotkey("ctrl", "w")
        time.sleep(0.2)
