'''products = ["OREO REESE'S Peanut Buttery Creme Chocolate Sandwich Cookies, Limited Edition, 10.81 oz",
            "OREO Orange Creme Chocolate Sandwich Cookies, Limited Edition, Halloween Cookies, 18.71 oz",
            "OREO Chocolate Sandwich Cookies, 13.29 oz",
            "OREO Double Stuf Chocolate Sandwich Cookies, Fam"]
for product in products:
    try:
        print(product)
        print(product.index("oz"))
        oz_index = product.index("oz")
        i = oz_index - 2
        while i >= 0 and (product[i].isdigit() or product[i] == '.'):
            i -= 1
        number_str = product[i:oz_index].strip()
        number = float(number_str)
        print("Number of oz:", number)
    except:
        print("No oz information")
'''
prices = ["$4.9726.6 ¢/oz", "$4.8845.1 ¢/oz"]
original_prices = []
prices_per_ounce = []
for price in prices:
    #$4.9726.6 ¢/oz

        dot_index = price.index(".")
        original_price = price[1:dot_index+3]
        print("Original price:", original_price)
        original_prices.append(float(original_price))
        space_index = price.index(" ")
        price_per_ounce = price[dot_index+3:space_index]
        print("price per ounce:", price_per_ounce)
        prices_per_ounce.append(float(price_per_ounce))
    #except:
        #print("Error in getting prices")
        #original_prices.append(0)
        #prices_per_ounce.append(0)

print(prices)
print(original_prices)
print(prices_per_ounce)
