from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re

filePath = "prometheus.html"

def getTextFromHtml(filePath):
    # prometheus.org.ua потребує cookies та має captcha
    # що унеможливлює зчитувати його html напряму за допомогою requests
    with open(filePath, "r", encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    return soup.get_text()

def makeDictOfWords(words, text):
    wordsDict = dict()
    for word in words:
        wordsDict[word] = len(re.findall(word, text.lower()))

    return wordsDict

data = makeDictOfWords({"дистанційна", "курс", "програмування"}, getTextFromHtml(filePath))
keys = list(data.keys())
values = list(data.values())
plt.bar(keys, values)

plt.xlabel('Слова')
plt.ylabel('Кількість')
plt.title('Гістограма слів')

plt.show()
