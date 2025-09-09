import pyautogui as pag
import time
import pyperclip
import pandas as pd
from bs4 import BeautifulSoup

#List of foods to search for
foods = ["prego sauce", "vanilla", "powdered sugar", "canola oil", "brown sugar", "cinnamon",
         "baking powder", "baking soda", "silk soy milk", "silk soy yogurt", "long grain rice",
         "sugar", "red kidney beans", "great northern beans", "birds eye streamfresh corn",
         "birds eye peas", "double-stuf oreos", "welches strawberry jelly", "aluminum foil",
         "gold medal flour", "club crackers", "imperial margarine", "Phish Food Non-Dairy Oat",
         "original lays chips",]

#Blank arrays to be filled with product information
products = []
prices = []
ounces = []
sources = []
prices_per_ounce = []
categories = []

def visitWebsite(link):
    """Helper function to visit a website using browser address bar + shortkeys"""
    pag.hotkey("ctrl", "l") #browser address bar
    pag.write(link, interval=0.1)
    pag.press('enter')
    time.sleep(4)

def findOunces(productTitle):
    """Find ounces using product title when not explicitly given"""
    total = 0
    productTitle = productTitle.lower()
    temparray = productTitle.split() #Split title into separate words
    if("oz" in temparray):
        if(temparray[temparray.index("oz")-1] == "fl"): #If in fl oz
            total = temparray[temparray.index("fl")-1]
        else: #if just in oz
            total = temparray[temparray.index("oz")-1]
    elif("lb" in temparray):
        total = 16*int(temparray[temparray.index("lb")-1])
    elif("gl" in temparray):
        total = 128*int(temparray[temparray.index("lb")-1])
    else:
        for item in temparray:
            if "lb" in item:
                try:
                    total = int(item[:item.index("lb")])
                except:
                    total = 0
        total = 0
    #TODO - Implement "pack of 3"
    return total

def findOuncesKroger(title, price, text):
    """Fixes Kroger's tendency to fix amount and price/amount in same field"""
    if("Â®" in title): #Remove the Registered symbol from product titles
        title = title[:title.index("Â®")] + title[title.index("Â®")+2:]

    if("$" in text): #If it grabbed price per amount instead of amount
        number = float(text[1:text.index("/")])
        try:
            ounces = float(price)/number
            text = ounces
        except:
            text = 0
    else: #It grabbed ounces correctly
        textarray = text.split()
        if("oz" in textarray or "fl oz" in textarray or "lb" in textarray):
            text = float(textarray[0])
    return title, price, text

def Kroger():
    """Kroger"""
    visitWebsite("kroger.com")
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
            product, price, ounce = findOuncesKroger(product.get_text(strip=True), price["value"], ounce.get_text(strip=True)) #Get text in good format
            print(product, ": ", price)
            products.append(product)
            prices.append(price)
            ounces.append(ounce)
            try: #Sometimes fails
                prices_per_ounce.append(float(price)/float(ounce))
            except:
                prices_per_ounce = 0
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

def Walmart():
    """Walmart"""
    visitWebsite("walmart.com")
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
            ounces.append(findOunces(product.get_text(strip=True)))
            prices_per_ounce.append(0)
            categories.append(foods.index(food))
            sources.append("Walmart")
            counter += 1
            if counter > 5:
                break #
        pag.hotkey("ctrl", "w")
        time.sleep(0.2)

def FoodCity():
    """Food City Function"""
    visitWebsite("foodcity.com")
    for food in foods:
        pag.moveTo(624, 238) #Search bar
        time.sleep(0.3)
        pag.click()
        time.sleep(0.3)
        pag.press('delete', presses=10)
        time.sleep(0.1)
        pag.write(food, interval=0.05) #type in food
        pag.press('enter')
        time.sleep(4)
        pag.hotkey("ctrl", "u")
        time.sleep(3)
        pag.hotkey("ctrl", "a")
        time.sleep(0.2)
        pag.hotkey("ctrl", "c")
        time.sleep(1)
        html = pyperclip.paste()
        soup = BeautifulSoup(html, "html.parser")
        product_titles = soup.find_all("span", {"class": "line-clamp--2"})
        temp_ounces = soup.find_all("span", {"class": "clearfix tile-item__product__size"})
        temp_prices = soup.find_all("span", {"class": "clearfix tile-item__product__price deal__"})
        #print("Found", len(product_titles), "titles and", len(temp_prices), "prices")
        counter = 0
        for product, ounce, price in zip(product_titles, temp_ounces, temp_prices):
            print(product.get_text(strip=True), ": ", price.get_text(strip=True))
            products.append(product.get_text(strip=True))

            try:
                text = ounce.get_text(strip=True)
                o_index = text.index("o")
                ounces.append(text[0:o_index])
            except ValueError:
                ounces.append(float(ounce.get_text(strip=True)))
            prices.append(price.get_text(strip=True))
            sources.append("Food City")
            counter += 1
            if counter > 5:
                break
        pag.hotkey("ctrl", "w")
        time.sleep(0.2)
'''
def Samsclub():
    visitWebsite("samsclub.com")
    for food in foods:
        pag.moveTo(752, 164) #Search bar
        time.sleep(0.3)
        pag.click()
        time.sleep(0.3)
        pag.press('delete', presses=10)
        time.sleep(0.1)
        pag.write(food, interval=0.05) #type in food
        pag.press('enter')
        time.sleep(4)
        pag.hotkey("ctrl", "r")
        time.sleep(4)
        pag.hotkey("ctrl", "u")
        time.sleep(3)
        pag.hotkey("ctrl", "a")
        time.sleep(0.2)
        pag.hotkey("ctrl", "c")
        time.sleep(1)
        pag.hotkey("ctrl", "c")
        time.sleep(1)
        html = pyperclip.paste()
        time.sleep(0.5)
        soup = BeautifulSoup(html, "html.parser")
        product_titles = soup.find_all("span", {"data-automation-id": "product-title"})
        print("Found", len(product_titles), "product titles")
        temp_prices = []
        price_containers = soup.find_all("div", {"data-automation-id": "product-price"})
        for container in price_containers:
            price_div = container.find("div", class_="mr1 mr2-xl b black lh-solid f5 f4-l")
            if price_div:
                temp_prices.append(price_div.get_text(strip=True)[1:])
        counter = 0
        for product, price in zip(product_titles, temp_prices):
            print(product.get_text(strip=True), ": ", price.get_text(strip=True))
            products.append(product.get_text(strip=True))
            ounces.append(0)
            prices.append(price.get_text(strip=True))
            sources.append("Samsclub")
            counter += 1
            if counter > 5:
                break
        pag.hotkey("ctrl", "w")
        time.sleep(0.2)
'''

time.sleep(2)
Kroger()
Walmart()
#FoodCity()
#Samsclub() - NOT WORKING

print("products")
print(products)
print("prices")
print(prices)
print("ounces")
print(ounces)
print("sources")
print(sources)

df = pd.DataFrame({ #Put into dataframe for saving as csv file
    'Product': products,
    'Price': prices,
    'Ounces': ounces,
    'Source': sources,
    'Price per ounce': prices_per_ounce,
    'Categories': categories
})
df.to_csv('grocery store.csv', index = False)
