from urllib import request
from bs4 import BeautifulSoup
from re import sub
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS


#Which wikipedia page you want to be opened, second line pretends to be a Web browser, many pages don´t open without it-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
page = request.Request('https://en.wikipedia.org/wiki/Computer_science')
page.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')


#Opens the page and transforms everything to an html-utf-8 code-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
page = request.urlopen(page)
page = page.read().decode('utf-8')
page = BeautifulSoup(page, 'html.parser')


#Selects the div that has the page's content and saves it all into a list, in the case of Wikipedia, the div with all the content is 'mw-parser-output'-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
list = []
for x in page.find_all('div', class_='mw-parser-output'):
    list.append(x.text)
    list.append(' ')


#Formmating of the page's content, removes everything that isn´t letters and spaces-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
final_string = ''.join(list)
final_string = final_string.upper()
final_string = sub(r'[^a-zA-Z\s]', '', final_string)


#Stopwords to be removed from the Wordcloud-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
list_stopwords = ['D','X','TWO','AUGUST','FORM','BECAME','USED','OCTOBER','FOUND','P','ADA','ISBN','APRIL','SEE','TERM','DENNING','IEEE','BABBAGE','DECEMBER','ONE','THREE','AIM','SCID','WAY','MAY','COMMON','DOI','B','DE','USE','ARGUED','FEBRUARY','CHARLES','ISBN','SEPTEMBER','OFTEN','C','MARCH','JUNE','J','S','NAME']
for i in list_stopwords:
    STOPWORDS.add(i)


#Wordcloud itself-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
wordcloud = WordCloud(width= 1920, height= 1080, collocations = False, background_color = 'white', colormap='plasma', stopwords=STOPWORDS).generate(final_string)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()





