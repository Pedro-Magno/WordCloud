import urllib.request
from bs4 import BeautifulSoup
import re
from collections import Counter

#Determina a página selecionada, segunda linha finge ser um browser normal, muitas páginas não aceitam abrir sem um browser
page = urllib.request.Request("https://en.wikipedia.org/wiki/Computer_science")
page.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')


#Abre a página e transforma tudo em um código html legível em utf-8
page = urllib.request.urlopen(page)
page = page.read().decode("utf-8")
page = BeautifulSoup(page, "html.parser")


#Seleciona a div que possui todo o conteúdo da página e salva o conteudo numa lista, no caso da Wikipedia todo o conteúdo se encontra na div de classe "mw-parser-output"
list = []
for x in page.find_all("div", class_="mw-parser-output"):
    list.append(x.text)
    list.append(" ")


#Formatação do conteúdo da página, remoção de caracteres não letras e separação por espaços das palavras
final_string = "".join(list)
final_string = final_string.upper()
final_string = re.sub(r'[^a-zA-Z\s]', '', final_string)
final_list = final_string.split()
final_dictionary = Counter(final_list)

https://www.wordexample.com/list/most-common-words-1k#google_vignette
print(Counter(final_list))


