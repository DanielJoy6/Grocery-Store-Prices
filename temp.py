from bs4 import BeautifulSoup

def find_ounces(text):
  print(text)
  if("perlb" in text):
    return 16
  if("perpk" in text):
     return 0
  if("oz" in text):
     return text[:text.index("oz")]
  return 0

html = """<span class="clearfix tile-item__product__size">
								2&nbsp;<abbr title="ounce">oz.</abbr>							</span>"""
soup = BeautifulSoup(html, "html.parser")
temp_ounces = soup.find_all("span", {"class": "clearfix tile-item__product__size"})

for item in temp_ounces:
    print(find_ounces(item.get_text(strip=True)))

