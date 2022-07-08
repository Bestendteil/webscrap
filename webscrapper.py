import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/jefferykwok/Downloads/chromedriver')
driver.get('https://oxylabs.io/blog')
results = []
otherresults = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for a in soup.findAll(attrs='post-preview'):
    name = a.find('h2')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='post-preview__meta'):
    date = b.find('p')
    if date not in results:
        results.append(date.text)

df = pd.DataFrame({'Names': results, 'Dates':otherresults})
df.to_csv('names.csv', index = False, header = True, sep = ',', encoding = 'utf-8')