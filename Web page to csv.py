import urllib.request
from bs4 import BeautifulSoup
import re
from collections import Counter
import ast
import csv

#Determina a página selecionada, segunda linha finge ser um browser normal, muitas páginas não aceitam abrir sem um browser
page = urllib.request.Request("https://en.wikipedia.org/wiki/Computer_science")
page.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')


#Abre a página e transforma tudo em um código html utf-8
page = urllib.request.urlopen(page)
page = page.read().decode("utf-8")
page = BeautifulSoup(page, "html.parser")


#Seleciona a div que possui o conteúdo da página e salva o conteudo numa lista, no caso da Wikipedia o conteúdo se encontra na div de classe "mw-parser-output"
list = []
for x in page.find_all("div", class_="mw-parser-output"):
    list.append(x.text)
    list.append(" ")


#Formatação do conteúdo da página, remoção de caracteres não letras e separação por espaços das palavras, transforma em um dicionário
final_string = "".join(list)
final_string = final_string.upper()
final_string = re.sub(r'[^a-zA-Z\s]', '', final_string)
final_list = final_string.split()
final_dictionary = str(Counter(final_list))
final_dictionary = final_dictionary.removesuffix(")").removeprefix("Counter(").strip()
final_dictionary =  ast.literal_eval(final_dictionary)

#Transforma o Dicionário em um arquivo csv
Dataframe = open('Dataframe.csv', 'w')
for key in final_dictionary.keys():
    Dataframe.write("%s, %s\n" % (key, final_dictionary[key]))

