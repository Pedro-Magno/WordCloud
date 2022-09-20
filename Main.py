import urllib.request
from bs4 import BeautifulSoup


page = urllib.request.Request("https://en.wikipedia.org/wiki/Computer_science")
page.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
page = urllib.request.urlopen(page)
file = page.BeautifulSoup.find("div", class_="mw-parser-output")
file = file.read().decode("utf-8")
file = BeautifulSoup(file, "html.parser")

print(file.get_text())

