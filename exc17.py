from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/"
session = requests.Session()
session.headers.update(
    {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

response = session.get(url)
print(response.status_code)
html = response.text

code = BeautifulSoup(html, "html.parser")

titles = code.select("div.css-xdandi")
# for num in range(0, len(titles)):
#     title = titles[num]
#     print(title.get_text())


titles_clean = [title.get_text() for title in titles]
print(titles_clean)
