# Grocery-Store-Prices

This program uses Python's PyAutoGui library to scrape Walmart + Kroger's websites for select items + prices. It calculates price/ounce and places the results into a CSV file for analysis.

## Current Approach
- The program uses PyAutoGui to navigate to websites and search for specific items
- The source code for that search result page is copied and pasted into Beautiful Soup, which detects product titles & prices
- Prices per ounce are calculated for a fair comparison between products
- Results are tagged with a category to find lowest price/ounce for each search term
- Results are exported to a csv to be cleaned up and examined.

## Example GIF
![MyGIF](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXY1Y20yeDA1YXk4b2t6MmMzaXF0ZzNhbGUzYTF6a3loMHEzd2MxNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NQR64tyRWubnP6y6Qy/giphy.gif)

## Installation Guide
1. Clone the repo
```
git clone https://github.com/USERNAME/Grocery-Store-Prices.git
cd Grocery-Store-Prices
```
2. Install required packages
```
pip install pyautogui bs4 pyperclip pandas 
```
3. Run main file
```
python main.py
```

## Packages Used
- PyAutoGui - mouse movement
- BeautifulSoup - HTML parsing
- Pyperclip - copy/pasting from clipboard
- Pandas - exporting to csv at end

## Future Improvements
- Multipack product detection ("Pack of 6")
- Better error handling than catch-all "excepts"
- Adding more grocery stores. Food City would be easy

My intiial attempt was through the requests library, which failed. Next was Selenium, which also failed, as all websites detected that I was a robot. I tried using only PyAutoGui, but it was too finicky.

There are still a lot of improvements to be made. Feel free to contribute through pull requests if you would like!

Contact: danieljoy2345@gmail.com
