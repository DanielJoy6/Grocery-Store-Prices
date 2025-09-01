import pyautogui as pag
import pydirectinput as directInput
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip

foods = ["oreos"]
products = []
prices = []
ounces = []
sources = []


def visitWebsite(link):
    pag.moveTo(621, 90) #browser address bar
    pag.click()
    pag.write(link, interval=0.1)
    pag.press('enter')
    time.sleep(4)

def Kroger():
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
        time.sleep(4)
        if(food == "oreos"):
            pag.scroll(-500) #Scroll down a bit
        else:
            pag.scroll(-370)
        time.sleep(0.5)

        for item in [(55, 667), (419, 660), (792, 660), (1157, 660), (1529, 660)]: #First 5 results
            pag.moveTo(item) #start of Product title
            time.sleep(0.5)
            pag.dragRel(285, 85, 0.5) #End of product title
            pag.hotkey('ctrl', 'c')
            time.sleep(1) #HERE
            title = pyperclip.paste()
            print(title)
            products.append(title)
            pag.mouseUp()
            time.sleep(1)

            pag.moveTo(item)
            pag.moveRel(0, -100, 0.5)
            pag.dragRel(87, 61, 0.5)
            pag.hotkey('ctrl', 'c')
            time.sleep(0.1)
            price = pyperclip.paste()
            print(price)
            prices.append(price)
            pag.mouseUp()
            sources.append("Kroger")
            
        pag.moveTo(28, 82, 1) #Back button
        pag.click()
        time.sleep(2)

def Walmart():
    visitWebsite("walmart.com")
    for food in foods:
        pag.moveTo(840, 170) #Search bar
        time.sleep(1)
        pag.click()
        time.sleep(1)
        pag.write(food, interval=0.2) #type in food
        pag.press('enter')
        time.sleep(5)
        pag.scroll(-10) #Scroll down a bit
        time.sleep(1)
        #First item - Point(x=564, y=770)
        #Second item - Point(x=913, y=765)
        #Third item - Point(x=1238, y=762)
        #Fourth item - Point(x=1642, y=766)
        for item in [(564, 770), (913, 765), (1238, 762), (1642, 766)]: #First 4 results
            pag.moveTo(item) #move to individual items
            time.sleep(1)
            pag.click()
            time.sleep(5)
            pag.moveTo(818, 392) #start of Product title
            time.sleep(0.5)
            pag.dragTo(1368, 470, 1) #End of product title
            pag.hotkey('ctrl', 'c')
            time.sleep(0.1)
            title = pyperclip.paste()
            print(title)
            products.append(title)
            time.sleep(1)
            pag.moveTo(1474, 340) #Start of price
            pag.dragTo(1648, 339, 1) #End of price
            pag.hotkey('ctrl', 'c')
            time.sleep(0.1)
            price = pyperclip.paste()
            print(price)
            prices.append(price)
            pag.moveTo(28, 82, 1) #Back button
            pag.click()
            time.sleep(2)
            source.append("Walmart")

def FoodCity():
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
        time.sleep(3)
        pag.scroll(-500)
        time.sleep(0.5)
        for item in [(208, 625), (568, 620), (1021, 618), (1422, 618)]: #First 5 results
            pag.moveTo(item) #start of Product title
            time.sleep(0.5)
            pag.dragRel(284, 65, 0.5) #End of product title
            pag.hotkey('ctrl', 'c')
            time.sleep(1) #HERE
            title = pyperclip.paste()
            print(title)
            products.append(title)
            pag.mouseUp()
            time.sleep(1)

            pag.moveTo(item)
            pag.moveRel(0, 82, 0.5) #Move to price start
            pag.dragRel(287, 3, 0.5) #Move to price end
            pag.hotkey('ctrl', 'c')
            time.sleep(0.1)
            price = pyperclip.paste()
            print(price)
            prices.append(price)
            pag.mouseUp()
            sources.append("Food City")
            
        pag.scroll(500)
        time.sleep(1)
        pag.moveTo(233, 248)
        time.sleep(0.1)
        pag.click()
        time.sleep(2)

def SamsClub():
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
        time.sleep(3)
        pag.scroll(-400)
        time.sleep(0.5)
        for point in [(204, 790), (590, 802), (957, 795), (1335, 792), (1705, 792)]:
            pag.moveTo(point)
            time.sleep(0.1)
            pag.click()
            time.sleep(5)

            pag.moveTo(1303, 507) #start of Product title
            time.sleep(0.3)
            pag.dragRel(560, 0, 0.5) #End of product title
            pag.hotkey('ctrl', 'c')
            time.sleep(1) #HERE
            title = pyperclip.paste()
            print(title)
            products.append(title)
            pag.mouseUp()
            time.sleep(0.5)

            pag.moveTo(1305, 606)
            pag.dragRel(250, 6, 0.5) #Move to price end
            pag.hotkey('ctrl', 'c')
            time.sleep(0.1)
            price = pyperclip.paste()
            print(price)
            prices.append(price)
            pag.mouseUp()
            sources.append("SamsClub")

            pag.moveTo(28, 82, 1) #Back button
            pag.click()
            time.sleep(4)
            

time.sleep(2)
SamsClub()
#FoodCity()
#Kroger()
#Walmart()

for product in products:
    try:
        oz_index = product.index("oz")
        i = oz_index - 2
        while i >= 0 and (product[i].isdigit() or product[i] == '.'):
            i -= 1
        number_str = product[i:oz_index].strip()
        number = float(number_str)
        ounces.append(number)
    except:
        print("Error in getting ounces")
        ounces.append(0)
original_prices = []
prices_per_ounce = []
for price in prices:#$4.9726.6 ¢/oz
    try:
        dot_index = price.index(".")
        original_price = price[1:dot_index+3]
        #print("Original price:", original_price)
        original_prices.append(float(original_price))
        space_index = price.index(" ")
        price_per_ounce = price[dot_index+3:space_index]
        #print("price per ounce:", price_per_ounce)
        prices_per_ounce.append(float(price_per_ounce))
    except:
        print("Error in getting prices")
        original_prices.append(0)
        prices_per_ounce.append(0)
print(products)
print(prices)
print(original_prices)
print(prices_per_ounce)
print(ounces)
print(sources)

import pandas as pd
df = pd.DataFrame(products, original_prices, prices_per_ounce, ounces, sources, columns=['Product', 'Price', 'Price Per Ounce', 'Ounces', 'Source'])
df.to_csv('grocery store.csv')



'''

stores = ["Kroger", "Walmart", "SamsClub", "Food City"]
#Walmart, Food City, Samsclub getable with requests
#Kroger, Costco need to manually do it

for store in stores:
    print("Store:", store, end=" ")
    if store == "Kroger":
        link = "https://www.kroger.com/"
    elif store == "Walmart":
        link = "https://www.walmart.com/"
    elif store == "Food City":
        link = "https://www.foodcity.com/"
    elif store == "SamsClub":
        link = "https://www.samsclub.com/"
    elif store == "Costco":
        link = "https://www.costco.com/"
    try:
        page = requests.get(link, timeout=5)
        print(page)
        print(page.status_code)
    except:
        print("Timed out")

print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
title = soup.title.string
print("Page Title:", title)

# Example: Extract all links on the page
for link in soup.find_all("a"):
    print(link.get("href"))

'''
#Option 1: Selenium driver
'''
driver = webdriver.Firefox()
driver.get("https://www.walmart.com/")
print(driver.title)
time.sleep(10)

element = driver.find_element(By.CLASS_NAME, "search-input-field-v2")
print("Found element", element)
element.click()
time.sleep(2)
element.clear()
element.send_keys(foods[0])
time.sleep(2)
element.send_keys(Keys.RETURN)
for x in range(30):
    print("Sleeping...", x)
    time.sleep(1)

elements = driver.find_elements(By.CLASS_NAME, "w_iUH7")
for element in elements:
    print("Item:", element)

time.sleep(5)
#Walmart search bar(x=840, y=170)

#Option 2: Requests package
link = "https://www.walmart.com/search?q=strawberry+jelly"
try:
    page = requests.get(link, timeout=5)
    print(page)
    print(page.status_code)
except:
    print("Timed out")


soup = BeautifulSoup(page.text, "html.parser")
title = soup.title.string
print("Page Title:", title)

# Example: Extract all links on the page
items = soup.find_all(class_='w_iUH7')

for item in items:
    print(item.get_text())

STOP

'''

