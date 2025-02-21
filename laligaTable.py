import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.skysports.com/la-liga-table"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_="sdc-site-table")

headers = [header.text.strip() for header in table.find_all("th")]

data = []
for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    data.append([col.text.strip() for col in cols])

df = pd.DataFrame(data, columns=headers)
df.to_csv("laligaTable.csv", index=False)