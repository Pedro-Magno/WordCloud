from urllib import request
from bs4 import BeautifulSoup
from re import sub
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS


#Determina a página selecionada, segunda linha finge ser um browser normal, muitas páginas não aceitam abrir sem um browser-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
page = request.Request("https://en.wikipedia.org/wiki/Computer_science")
page.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')


#Abre a página e transforma tudo em um código html utf-8-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
page = request.urlopen(page)
page = page.read().decode("utf-8")
page = BeautifulSoup(page, "html.parser")


#Seleciona a div que possui o conteúdo da página e salva o conteudo numa lista, no caso da Wikipedia o conteúdo se encontra na div de classe "mw-parser-output"-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
list = []
for x in page.find_all("div", class_="mw-parser-output"):
    list.append(x.text)
    list.append(" ")


#Formatação do conteúdo da página, remoção de caracteres não letras-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
final_string = "".join(list)
final_string = final_string.upper()
final_string = sub(r'[^a-zA-Z\s]', '', final_string)


#Stopwords a serem removidos do Wordcloud-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
lista_stopwords = ["D","X","TWO","AUGUST","FORM","BECAME","USED","OCTOBER","FOUND","P","ADA","ISBN","APRIL","SEE","TERM","DENNING","IEEE","BABBAGE","DECEMBER","ONE","THREE","AIM","SCID","WAY","MAY","COMMON","DOI","B","DE","USE","ARGUED","FEBRUARY","CHARLES","ISBN","SEPTEMBER","OFTEN","C","MARCH","JUNE","J","S","NAME"]
for i in lista_stopwords:
    STOPWORDS.add(i)


#Wordcloud em si-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
wordcloud = WordCloud(width= 1920, height= 1080, collocations = False, background_color = 'white', colormap='plasma', stopwords=STOPWORDS).generate(final_string)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()





