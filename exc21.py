from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/"
session = requests.Session()
session.headers.update(
    {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})


response = session.get(url)
print(response.status_code)
html = response.text

soup = BeautifulSoup(html, "html.parser")

elements = soup.select('.story-wrapper a')


titles_clean = [ele.select_one(
    '.indicate-hover').get_text(strip=True) for ele in elements if ele.select_one('.indicate-hover')]

filename = input("please enter filename")

with open(filename, 'w', encoding="utf-8") as f:
    for ele in titles_clean:
        f.write(f"{ele}\n")
