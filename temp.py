"""Temporary testing file"""
import time
import pandas as pd
from target import target

foods = ["banana"]

products = []
prices = []
ounces = []
sources = []
prices_per_ounce = []
categories = []

time.sleep(3)
target(foods, products, prices, ounces, sources, prices_per_ounce, categories)
time.sleep(1)
df = pd.DataFrame({
    'Product': products,
    'Price': prices,
    'Ounces': ounces,
    'Source': sources,
    'Price per ounce': prices_per_ounce,
    'Categories': categories
})
df.to_csv('temporary grocery store.csv', index = False)
