#from bs4 import BeautifulSoup
'''
html = '''
#<div role="group" data-item-id="13609818113" data-dca-guid="13609818113" data-dca-id="13609818113" data-dca-name="ui_product_tile:vertical_index" data-dca-type="module" class="sans-serif mid-gray relative flex flex-column w-100 hide-child-opacity"><a link-identifier="13609818113" class="w-100 h-100 z-1 hide-sibling-opacity  absolute" target="" href="https://www.samsclub.com/midas/sams-crs/track?bt=1&amp;eventST=click&amp;plmt=sp-search-middle~desktop~&amp;pos=1&amp;tax=100001&amp;rdf=1&amp;rd=https%3A%2F%2Fwww.samsclub.com%2Fip%2FLay-s-Wavy-Original-Potato-Chips-15-625-oz%2F13609818113%3FclassType%3DREGULAR&amp;adUid=513a15b1-8cc0-4047-9270-a2f5cb4ae09f&amp;mloc=sp-search-middle&amp;pltfm=desktop&amp;pgId=original%20lays%20chips&amp;pt=search&amp;spQs=X8uUfUOBzJStxoJcGRAqw32SE-0LL1Km32IEclU63ZDfAZC-d33LWwTbPvkgkH3M2nRAVMlBc6Wx-JS_xjyIXa2mY9ApMhg4MqoD53SsUhjTHMa8zdD3-PCzANSKUoEg5RuabB2_U0jyHle4O7__rlmYsqqY1WY2RC3PDDkOQDSX9UI2CTP7dayh3j4MDIz6hzBo_twThyppdRMZ04-byG2R4SZ6X2AbhiS3aQ6ZXFtp1VqrkFhoFC3-R1CsTa-W8giACmhns8Pk3vX27UQ4TQ&amp;storeId=8256&amp;specificity=&amp;specificityScore=&amp;bkt=ace1_default%7Cace2_default%7Cace3_default&amp;classType=REGULAR"><span class="w_q67L">Lay's Wavy Original Potato Chips, 15.625 oz. </span></a><div class="" data-testid="list-view"><div class=""><div class=""><div class="h2 relative nowrap mb1"></div><div class="relative" data-testid="item-stack-product-image-flag-container"><div class="relative overflow-hidden" style="max-width: 290px; height: 0px; padding-bottom: min(290px, 100%); align-self: center; width: min(290px, 100%);"><img loading="eager" srcset="https://i5.walmartimages.com/asr/9d1b0612-9c92-42b4-911f-8d02f1cb44f9.39aefbbb1b378c690713b80e6a0c3b2e.jpeg?odnHeight=290&amp;odnWidth=290&amp;odnBg=FFFFFF 1x, https://i5.walmartimages.com/asr/9d1b0612-9c92-42b4-911f-8d02f1cb44f9.39aefbbb1b378c690713b80e6a0c3b2e.jpeg?odnHeight=580&amp;odnWidth=580&amp;odnBg=FFFFFF 2x" src="https://i5.walmartimages.com/asr/9d1b0612-9c92-42b4-911f-8d02f1cb44f9.39aefbbb1b378c690713b80e6a0c3b2e.jpeg?odnHeight=580&amp;odnWidth=580&amp;odnBg=FFFFFF" id="is-0-productImage-0" width="" height="" class="absolute top-0 left-0" data-testid="productTileImage" alt="Lay's Wavy Original Potato Chips, 15.625 oz."></div><div class="z-2 relative mt3 flex flex-wrap"><div class="relative dib flex-row-reverse" data-id=""><button class="w_eEg0 w_OoNT w_4QgR" type="button" data-pcss-hide="true" data-automation-id="atc" data-dca-id="cart_add_to_cart:add_to_cart_variant:blue_button_13609818113" data-dca-intent="cartAddition" data-dca-name="ItemBuyBoxAddToCartButton" aria-label="Add to Cart - Lay's Wavy Original Potato Chips, 15.625 oz."><div style="position: relative;"><span data-pcss-hide="true" style="visibility: visible;">Add to Cart</span></div></button></div><button aria-label="Add to list Lay's Wavy Original Potato Chips, 15.625 oz." class="w_3uZh w_wzOT bg-white ml2" type="button" style="border: 1px solid rgb(167, 183, 196); flex-shrink: 0;"><img loading="lazy" src="//i5.walmartimages.com/dfw/63fd9f59-ecc9/905da406-b102-4b3c-b55f-83be861ea022/v1/sams-lists.svg" width="16" height="16" alt=""></button></div></div><div class="mt2 mb1" style="height: 24px;" data-testid="variant-13609818113"><div class="flex items-center lh-title h2-l normal"><div class="flex items-center f7"><div>Sponsored</div></div></div></div></div><div class=""><div><div data-automation-id="product-price" class="flex flex-wrap justify-start items-center lh-title mb1"><div class="mr1 mr2-xl b black lh-solid f5 f4-l" aria-hidden="true">$4.48</div><span class="w_q67L">current price $4.48</span><div data-testid="product-price-per-unit" class="gray mr1 f7 f6-l">$0.29/oz</div></div></div><span class="w_vi_D" style="-webkit-line-clamp: 3; padding-bottom: 0.125em; margin-bottom: -0.125em;"><span data-automation-id="product-title" class="normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy">Lay's Wavy Original Potato Chips, 15.625 oz.</span></span><div class="mb2 mt2"><span class="w_q67L">Available for Shipping , Pickup  or Delivery </span><span class="w_SrYk w_2ioM w_DNAl w_OAJ4 w_GNSW mr1 mt1 ph2" aria-hidden="true"><span class="w_pFVL"><i class="ld ld-Truck" style="font-size: 1rem; vertical-align: -0.175em; width: 1rem; height: 1rem; box-sizing: content-box;" aria-hidden="true"></i></span>Shipping </span><span class="w_SrYk w_2ioM w_DNAl w_OAJ4 w_GNSW mr1 mt1 ph2" aria-hidden="true"><span class="w_pFVL"><i class="ld ld-Pickup" style="font-size: 1rem; vertical-align: -0.175em; width: 1rem; height: 1rem; box-sizing: content-box;" aria-hidden="true"></i></span>Pickup </span><span class="w_SrYk w_2ioM w_DNAl w_OAJ4 w_GNSW mr1 mt1 ph2" aria-hidden="true"><span class="w_pFVL"><i class="ld ld-Delivery" style="font-size: 1rem; vertical-align: -0.175em; width: 1rem; height: 1rem; box-sizing: content-box;" aria-hidden="true"></i></span>Delivery </span></div></div></div></div></div>
'''
soup = BeautifulSoup(html, "html.parser")
product_titles = soup.find_all("span", {"data-automation-id": "product-title"})
for product in product_titles:
    print(product.get_text(strip=True))

price_containers = soup.find_all("div", {"data-automation-id": "product-price"})
for container in price_containers:
    price_div = container.find("div", class_="mr1 mr2-xl b black lh-solid f5 f4-l")
    if price_div:
       print(price_div.get_text(strip=True)[1:])

temparray = text.split()
if("oz" in temparray):
    if(temparray[temparray.index("oz")-1] == "fl"):
        print(temparray[temparray.index("fl")-1])
    else:
        print(temparray[temparray.index("oz")-1])
elif("lb" in temparray):
    print(16*int(temparray[temparray.index("lb")-1]))
else:
    for item in temparray:
        if "lb" in item:
            print(int(item[:item.index("lb")]))
'''
title = "PregoÂ® Homestyle Alfredo Pasta Sauce"
price = 2.79
text = "2 lb"
if(title.index("Â®") != 0):
    title = title[:title.index("Â®")] + title[title.index("Â®")+2:]

if("$" in text):
    number = float(text[1:text.index("/")])
    ounces = price/number
    text = ounces
else:
    textarray = text.split()
    if("oz" in textarray or "fl oz" in textarray or "lb" in textarray):
        text = float(textarray[0])
print(title, price, text)
    







