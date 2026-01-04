import pandas as pd
import streamlit as st
from pathlib import Path

store_colors = {
    "Walmart": "#ecec3d",     # Walmart Blue
    "Target": "#cc0000",      # Target Red
    "Publix": "#007a33",      # Publix Green
    "Kroger": "#ffffff",      # Kroger Blue
    "Trader Joe's": "#ff8d47", # Trader Joe's Red
    "Food City": "#d62828",
    "SamsClub": "#004B8D"
}


st.set_page_config(page_title="Grocery Price Comparator", layout="wide")
st.title("Grocery Price Comparator")
st.markdown("""
<style>
/* Make dataframe text bigger */
[data-testid="stDataFrame"] {
    transform: scale(1.55);
    transform-origin: top left;
}
[data-testid="stDataFrame"] > div {
    width: 100% !important;
}
</style>
""", unsafe_allow_html=True)


all_data = []
for file in Path("data").glob("*.csv"):
    df = pd.read_csv(file, encoding="latin1")
    all_data.append(df)

df = pd.concat(all_data, ignore_index=True)

# ---------- Category Mapping ----------
category_map = {
    0: "Mott Applesauce Cinnamon",
    1: "Hormel Black Label Bacon Fully Cooked Bacon",
    2: "Baking Powder",
    3: "Baking Soda",
    4: "Banana",
    5: "Basil",
    6: "Blueberries",
    7: "Broccoli",
    8: "Brown Sugar",
    9: "Imperial Margarine",
    10: "Chunk Chicken Breast",
    11: "Canned Diced Tomatoes",
    12: "Dark Red Kidney Beans",
    13: "Great Northern Beans",
    14: "Carrots",
    15: "Celery Stalks",
    16: "Cherry Cokes",
    17: "Boneless Chicken Breasts",
    18: "Enjoy Life Chocolate Chips",
    19: "Cinnamon",
    20: "Club Crackers",
    21: "Cocoa Powder",
    22: "Corn on the Cob",
    23: "Corn Starch",
    24: "Dry Basil",
    25: "Daiya Cheese Cheddar Shreds",
    26: "Flour",
    27: "Frozen Banana Slices",
    28: "Frozen Strawberries",
    29: "Frozen Corn",
    30: "Gala Apples",
    31: "Garlic",
    32: "Granny Smith Apples",
    33: "Green Bell Pepper",
    34: "Green Grapes",
    35: "Quaker Grits",
    36: "Ground Beef",
    37: "Honey",
    38: "Instant Pudding",
    39: "Joy Oreos",
    40: "Lays Original Chips",
    41: "Romane Lettuce",
    42: "Marinara Sauce",
    43: "Silk Soy Milk",
    44: "Quaker Oats",
    45: "Canola Oil",
    46: "Olive Oil",
    47: "White Onion",
    48: "Red Onion",
    49: "Yellow Onion",
    50: "Orange Bell Pepper",
    51: "Tropicana Orange Juice",
    52: "Oranges",
    53: "Oreos",
    54: "Pineapple",
    55: "Porkchop",
    56: "Powdered Sugar",
    57: "Purple Grapes",
    58: "Red Bell Pepper",
    59: "White Long Grain Rice",
    60: "Russet Potatoes",
    61: "Salt",
    62: "Shortening",
    63: "Soy Whipping Cream",
    64: "Spinach",
    65: "Pam Spray",
    66: "Strawberries",
    67: "Welches Strawberry Jelly",
    68: "Granulated Sugar",
    69: "Tide Pods",
    70: "Tomatoes",
    71: "Tomato Sauce",
    72: "Vanilla Extract",
    73: "Vegetable Broth",
    74: "Vinegar",
    75: "Watermelon",
    76: "Active-Dry Yeast",
    77: "Yellow Bell Pepper",
    78: "Silk Soy Yogurt",
    79: "Zucchini",
}


df["category_name"] = df["Categories"].map(category_map)

df["Price per ounce"] = pd.to_numeric(df["Price per ounce"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Ounces"] = pd.to_numeric(df["Ounces"], errors="coerce")

selected_category = st.selectbox(
    "Choose a category:", sorted(df["category_name"].dropna().unique())
)

filtered = df[df["category_name"] == selected_category]
filtered = filtered.sort_values("Price per ounce")

st.subheader(f"Results for {selected_category}")
display_df = filtered[[
    "Product",
    "Price",
    "Ounces",
    "Source",
    "Price per ounce"
]].copy()

display_df["Price"] = display_df["Price"].map(lambda x: f"{x:.2f}")
display_df["Ounces"] = display_df["Ounces"].map(lambda x: f"{x:.2f}")
display_df["Price per ounce"] = display_df["Price per ounce"].map(lambda x: f"{x:.3f}")

def color_store(val):
    color = store_colors.get(val, "#000000")
    return f"color: {color}; font-weight: 600;"
def shade_rows(row):
    if row.name % 2 == 0:
        return ["background-color: #f4f6f8"] * len(row)
    else:
        return [""] * len(row)

styled = (
    display_df.style.applymap(color_store, subset=["Source"])
)

st.dataframe(
    styled,
    width='stretch'
)

#TODO
#Change colors of Source/Store column to be color of store - Walmart Blue/Yellow, Trader Joes - Brown/Red
#Make option for Entire Table combined in one
#Add Target? Maybe
#Add images
