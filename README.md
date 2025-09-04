# Grocery-Store-Prices

I wrote this program to try and automatically get grocery store prices.

## Current Approach
- The program uses PyAutoGui to navigate to websites and search for specific items
- The source code for that webpage is copied and pasted into Beautiful Soup, which detects product titles & prices
- Results are exported to a csv to be cleaned up and examined



My intiial attempt was through the requests library, which failed. Next was Selenium, which also failed, as all websites detected that I was a robot. I tried using only PyAutoGui, but it was too finicky.


Currently, there are lots of improvements to be made! Feel free to contribute if you can
