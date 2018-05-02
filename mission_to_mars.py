
# coding: utf-8

# In[1]:


#Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from selenium import webdriver
import pandas as pd
import time
from os import getcwd
from os.path import join


# In[2]:


#set up splinter browser
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)


# In[3]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[4]:


#get url 
html = requests.get(url)
print(html)


# In[5]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = bs(html, 'html.parser')
print(news_soup.prettify())


# In[8]:


news_soup.body


# In[10]:


results = news_soup.find_all(class_='content_title')
results


# In[12]:


news_title= results[0].text
news_title


# In[14]:


results1=news_soup.find_all(class_='rollover_description_inner')


# In[15]:


p_news= results1[0].text
print(p_news)


# In[16]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
browser.click_link_by_partial_text('FULL IMAGE')

html=browser.html
soup=bs(html, "html.parser")

body = soup.find_all('body')
result = soup.find_all('img',class_='fancybox-image')


# In[17]:


results = soup.find('body')


# In[18]:


second_half= results.find_all('a', class_='button fancybox')[0]['data-fancybox-href']

first_half = "https://www.jpl.nasa.gov"

featured_image_url = first_half+second_half


print(featured_image_url)


# In[19]:


#websites that needs to be scrapped
url = 'https://twitter.com/marswxreport?lang=en'

html = requests.get(url)
print(html)

soup = bs(html.text, 'html.parser')

print(soup.prettify())


# In[20]:


soup.find('body')


# In[21]:


res= soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')

mars_weather= res[0].text

print(mars_weather)


# In[22]:


import pandas as pd
url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
tables


# In[23]:


df = tables[0]
df.columns = ['Planet Profile', 'Values']

df


# In[24]:


html_table = df.to_html()
html_table


# In[25]:


html_table.replace('\n', '')


# In[26]:


df.to_html('table.html')

# !open table.html

df.to_html('mars_facts.html')

soup=bs(open("mars_facts.html"),"html.parser")
    ## Stripping the soup data and saving in mars_facts disctionary, mars_info is a temperory list used
mars_info=[]
mars_facts={}
for z in soup.table('td'):
    #print(z.text)
    mars_info.append(z.text.strip(':'))
mars_facts=dict([(k, v) for k,v in zip (mars_info[::2], mars_info[1::2])])
print(mars_facts)
   


# In[27]:


mars_info1=[]

mars_info1.append(mars_facts)

print(mars_info1)


# In[28]:


#websites that needs to be scrapped
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

#Retrieve page with the requests module
html = requests.get(url)
print(html)

soup = bs(html.text, 'html.parser')

print(soup.prettify())


# In[29]:


soup.find('body')


# In[30]:


rel = soup.find_all(class_='itemLink product-item')


# In[31]:


rel1 = soup.find_all(class_='thumb')


# In[32]:


rel1[0]['src']


# In[33]:


title=[]
for titles in rel:
    title.append(titles.text)
    


# In[34]:


urls=[]

for url in rel1:
    image_url="https://astrogeology.usgs.gov/"+url['src']
    urls.append(image_url)


# In[35]:


hemisphere_image_urls=[]
i=0
for i in range(4):
    d = {"title":title[i], "image_url":urls[i]}
    hemisphere_image_urls.append(d)



# In[36]:


hemisphere_image_urls

