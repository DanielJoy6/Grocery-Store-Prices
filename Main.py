""" This program gets grocery store prices from Kroger and Walmart and puts them a csv file"""
import time
import pandas as pd
from kroger import kroger
from walmart import walmart
from target import target
from food_city import food_city

#List of foods to search for

fruit = ["banana", "welches strawberry jelly", "strawberries", "watermelon slices",
         "granny smith apples"]
veggies = ["birds eye streamfresh corn","birds eye peas", "russet potatoes",
           "shredded carrots", "celery", "zucchini", "vegetable broth",
           "white onion", "spinach"]
meat = ["porkchop loin chop boneless", "chicken breasts boneless"]
dairy = ["silk soy milk", "silk soy yogurt", "daiya non-dairy cheddar cheese"]
other = ["traditional prego sauce","red kidney beans", "great northern beans", "long grain rice",
       "italian seasoning", "cherry coke"]
baking = ["granulated sugar", "All-purpose flour", "vanilla", "powdered sugar",
          "canola oil", "brown sugar", "cinnamon", "baking powder", "baking soda",
          "imperial margarine"]
snacks = ["double-stuf oreos", "Phish food non-dairy oat", "original lays chips", "club crackers"]

foods = fruit + veggies + meat + dairy + other + baking + snacks

foods = ["Mott Applesauce Cinnamon", #0
         "Hormel Black label Bacon fully cooked bacon",
         "Baking Powder",
         "Baking Soda",
         "Banana", #4
         "Basil",
         "Blueberries",
         "Broccoli",
         "Brown Sugar",
         "Imperial Margarine",
         "Chunk Chicken Breast", #10
         "Canned Diced Tomatoes",
         "Dark Red Kidney Beans",
         "Great Northern Beans",
         "Carrots",
         "Celery Stalks", #15
         "Cherry Cokes",                                  
         "Boneless chicken breasts",
         "Enjoy life chocolate chips",
         "cinnamon",
         "club crackers", #20
         "cocoa powder",
         "corn on the cob",
         "corn starch",
         "dry basil",
         "daiya cheese cheddar shreds", #25
         "flour",
         "Frozen banana slices",
         "Frozen strawberries",
         "Frozen corn",
         "Gala Apples", #30
         "Garlic",
         "Granny Smith Apples",
         "Green Bell Pepper",
         "Green grapes",
         "Quaker Grits", #35
         "Ground Beef",
         "Honey",
         "Instant Pudding",
         "Joy Oreos",
         "Lays original chips", #40
         "Romane Lettuce",
         "Marinara Sauce",
         "Silk soy milk",
         "Quaker Oats",
         "Canola Oil", #45
         "Olive Oil",
         "White Onion",
         "Red Onion",
         "Yellow Onion",
         "Orange Bell Pepper", #50
         "Tropicana Orange Juice",
         "Oranges",
         "Oreos", 
         "Pineapple",
         "Porkchop", #55
         "Powdered Sugar",
         "Purple grapes",
         "Red Bell Pepper",
         "White long grain rice",
         "Russet Potatoes", #60
         "Salt",
         "Shortening",
         "Soy whipping cream",
         "Spinach",
         "Pam spray", #65
         "Strawberries",
         "Welches Strawberry Jelly",
         "Granulated Sugar",
         "Tide Pods",
         "Tomatoes", #70
         "Tomato sauce",
         "Vanilla Extract",
         "Vegetable Broth",
         "Vinegar",
         "Watermelon", #75
         "Active-Dry Yeast",
         "Yellow Bell Pepper",
         "Silk soy yogurt",
         "Zucchini"] #79

#foods = ["Silk soy yogurt"]
#Blank arrays to be filled with product information
products = []
prices = []
ounces = []
sources = []
prices_per_ounce = []
categories = []

time.sleep(2)

food_city(foods, products, prices, ounces, sources, prices_per_ounce, categories)
time.sleep(1)
df = pd.DataFrame({ #Put into dataframe for saving as csv file
    'Product': products,
    'Price': prices,
    'Ounces': ounces,
    'Source': sources,
    'Price per ounce': prices_per_ounce,
    'Categories': categories
})
print("products:", len(products))
print("prices:", len(prices))
print("ounces:", len(ounces))
print("sources:", len(sources))
print("prices per ounces:", len(prices_per_ounce))
print("categories:", len(categories))
print(products)
print(prices)
print(ounces)
print(prices_per_ounce)
print(categories)

df.to_csv('Food City Results.csv', index = False)
"""
target(foods, products, prices, ounces, sources, prices_per_ounce, categories)
time.sleep(1)
df = pd.DataFrame({ #Put into dataframe for saving as csv file
    'Product': products,
    'Price': prices,
    'Ounces': ounces,
    'Source': sources,
    'Price per ounce': prices_per_ounce,
    'Categories': categories
})
df.to_csv('grocery store2.csv', index = False)


kroger(foods, products, prices, ounces, sources, prices_per_ounce, categories)
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
df.to_csv('Kroger Results.csv', index = False)

walmart(foods, products, prices, ounces, sources, prices_per_ounce, categories)

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
df.to_csv('Walmart Results Yogurt.csv', index = False)
"""