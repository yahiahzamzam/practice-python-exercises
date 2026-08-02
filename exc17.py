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

# titles = []
# for ele in elements:
#     title = ele.select_one('.indicate-hover')
#     if title:
#         title_cl = title.get_text(strip=True)
#         titles.append(title_cl)

# print(titles)


titles_clean = [ele.select_one(
    '.indicate-hover').get_text(strip=True) for ele in elements if ele.select_one('.indicate-hover')]
print(titles_clean)


# gemini error handling extra
# try:
#     response = session.get(url, timeout=10)
#     # Automatically raises an exception for 4xx or 5xx server errors
#     response.raise_for_status()

#     soup = BeautifulSoup(response.text, "html.parser")

#     # FIX: Target semantic headline wrappers instead of dynamic class names
#     # NYT generally wraps main story headlines in <h3> elements
#     titles = soup.select("section.story-wrapper h3, .indicate-hover")

#     # Strip whitespace cleanly and filter out any accidental empty strings
#     titles_clean = [title.get_text(strip=True)
#                     for title in titles if title.get_text(strip=True)]

#     print(f"Successfully scraped {len(titles_clean)} titles:")
#     print(titles_clean)

# except requests.exceptions.RequestException as e:
#     print(f"An error occurred while fetching the page: {e}")
