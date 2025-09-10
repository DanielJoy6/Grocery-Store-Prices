# Grocery-Store-Prices

This program uses Python's PyAutoGui library to scrape Walmart + Kroger's websites for select items + prices. It calculates price/ounce and places the results into a CSV file for analysis.

## Current Approach
- The program uses PyAutoGui to navigate to websites and search for specific items
- The source code for that search result page is copied and pasted into Beautiful Soup, which detects product titles & prices
- Prices per ounce are calculated for a fair comparison between products
- Results are tagged with a category to find lowest price/ounce for each search term
- Results are exported to a csv to be cleaned up and examined.

## Packages Used
- PyAutoGui - mouse movement
- BeautifulSoup - HTML parsing
- Pyperclip - copy/pasting from clipboard
- Pandas - exporting to csv at end


My intiial attempt was through the requests library, which failed. Next was Selenium, which also failed, as all websites detected that I was a robot. I tried using only PyAutoGui, but it was too finicky.

There are still a lot of improvements to be made, such as detecting when a product title has "Pack of 6" or "3-pack". Feel free to contribute through pull requests if you would like.
Contact: danieljoy2345@gmail.com
