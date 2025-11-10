
def food_city():
    """Food City Function"""
    visit_website("foodcity.com")
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
