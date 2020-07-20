import requests
from bs4 import BeautifulSoup
from datetime import date

base_url = "https://www.myfitnesspal.com/food/diary/{name}?date={date}"
base_url = base_url.replace("{name}", "anthonymlock")
base_url = base_url.replace("{date}", date.today().isoformat())
page = requests.get(base_url)

# document.getElementsByClassName("total")[0].children[6].innerText
soup = BeautifulSoup(page.content, 'html.parser')

totals = soup.find('tr', class_="total")
cols = totals.find_all('td')


def get_int_from_html(html) -> int :
    tmpInner = html.find_all("span", class_="macro-value")
    if len(tmpInner) != 0 :
        return int(tmpInner[0].get_text())
    else: 
        return int(html.get_text())


calories = get_int_from_html(cols[1])
carbs = get_int_from_html(cols[2])
fat = get_int_from_html(cols[3])
protein = get_int_from_html(cols[4])
Sodium = get_int_from_html(cols[5])
sugar = get_int_from_html(cols[6])

print(f"cal {calories}")
print(f"carbs {carbs}")
print(f"fat {fat}")
print(f"protein {protein}")
print(f"Sodium {Sodium}")
print(f"sugar {sugar}")
