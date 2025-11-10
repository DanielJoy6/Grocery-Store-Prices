""" This program gets grocery store prices from Kroger and Walmart and puts them a csv file"""
import time
import pandas as pd
from kroger import kroger
from walmart import walmart

#List of foods to search for

veggies = ["birds eye streamfresh corn","birds eye peas", "russet potatoes",
           "shredded carrots", "celery", "zucchini", "vegetable broth",
           "white onion"]
fruit = ["banana", "welches strawberry jelly", "strawberries", "watermelon slices",
         "granny smith apples"]
meat = ["porkchop loin chop boneless", "chicken breasts boneless"]
dairy = ["silk soy milk", "silk soy yogurt", "daiya non-dairy cheddar cheese"]
odd = ["traditional prego sauce","red kidney beans", "great northern beans", "long grain rice",
       "italian seasoning"]
baking = ["granulated sugar", "All-purpose flour", "vanilla", "powdered sugar",
          "canola oil", "brown sugar", "cinnamon", "baking powder", "baking soda",
          "imperial margarine"]
snacks = ["double-stuf oreos", "Phish food non-dairy oat", "original lays chips", "club crackers"]


foods = veggies+fruit+meat+dairy+odd+baking+snacks

#Blank arrays to be filled with product information
products = []
prices = []
ounces = []
sources = []
prices_per_ounce = []
categories = []


time.sleep(2)
kroger(foods, products, prices, ounces, sources, prices_per_ounce, categories)
walmart(foods, products, prices, ounces, sources, prices_per_ounce, categories)
#FoodCity()
#Samsclub() - NOT WORKING

print("products:", len(products))
print("prices:", len(prices))
print("ounces:", len(ounces))
print("sources:", len(sources))
print("prices per ounces:", len(prices_per_ounce))
print("categories:", len(categories))

df = pd.DataFrame({ #Put into dataframe for saving as csv file
    'Product': products,
    'Price': prices,
    'Ounces': ounces,
    'Source': sources,
    'Price per ounce': prices_per_ounce,
    'Categories': categories
})
df.to_csv('grocery store.csv', index = False)
