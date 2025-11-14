"""Helper file for all Food City Stuff"""
import time
import pyautogui as pag
import pyperclip
from bs4 import BeautifulSoup

def find_ounces(text):
    """Helper function to parse through different sizes"""
    print(text)
    if "fl oz" in text:
        try:
            return text[:text.index("fl oz")]
        except:
            return text[:text.index("floz")]
    if "perlb" in text:
        return 16
    if "oz" in text:
        return text[:text.index("oz")]
    if "lb" in text:
        return text[:text.index("lb")]
    return 0


def food_city(foods, products, prices, ounces, sources, prices_per_ounce, categories):
    """Food City Function"""
    pag.hotkey("ctrl", "l") #browser address bar
    pag.write("foodcity.com", interval=0.1)
    pag.press('enter')
    time.sleep(4)
    print("Switching to Food City.. 5 seconds")
    pag.hotkey("ctrl", "shift", "i") #Open inspect
    time.sleep(1)
    for food in foods:
        pag.moveTo(240, 291) #Search bar
        time.sleep(0.5)
        pag.click()
        time.sleep(0.5)
        pag.hotkey("ctrl", "a")
        time.sleep(0.2)
        pag.press("delete")
        time.sleep(0.1)
        pag.write(food, interval=0.1) #type in food
        pag.press('enter')
        time.sleep(3)
        pag.moveTo(1238, 483)
        time.sleep(0.5)
        pag.click()
        time.sleep(0.1)
        pag.hotkey("ctrl", "c")
        time.sleep(1)
        html = pyperclip.paste()
        soup = BeautifulSoup(html, "html.parser")
        product_titles1 = soup.find_all("span", {"class": "d-block truncate-1"})
        product_titles2 = soup.find_all("span", {"class": "line-clamp--2"})
        temp_ounces = soup.find_all("span", {"class": "clearfix tile-item__product__size"})
        temp_prices = soup.find_all("span", {"class": "clearfix tile-item__product__price deal__"})
        print("Found", len(product_titles1), len(product_titles2), "titles,",
              len(temp_ounces), "ounces, and", len(temp_prices), "prices")
        counter = 0
        for p1, p2, ounce_element, price_element in zip(product_titles1, product_titles2, temp_ounces, temp_prices):
            full_title = p1.get_text(strip=True) + " " + p2.get_text(strip=True)
            price = price_element.get_text(strip=True)
            #print(full_title, ": ", price)
            products.append(full_title)
            try:
                ounce = find_ounces(ounce_element.get_text(strip=True))
            except TypeError:
                print("Error fetching ounces")
                ounce = 0.0
            try:
                price = price.split('$')[-1]
            except TypeError:
                print("Error fetching price")
                price = 0.0
            try:
                price_per_ounce = price/ounce
            except TypeError:
                price_per_ounce = 0
            try:
                prices.append(float(price))
            except ValueError:
                prices.append(price)
            ounces.append(ounce)
            prices_per_ounce.append(price_per_ounce)
            categories.append(foods.index(food))
            sources.append("Food City")
            counter += 1
            if counter > 5:
                break
