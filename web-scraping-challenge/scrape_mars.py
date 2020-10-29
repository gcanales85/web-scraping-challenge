#Dependencies
import time
import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs
from splinter import Browser

def init_browser():
    executable_path = {'executable_path': driverPath[0]}
    browser = Browser('chrome', **executable_path, headless=False)
    time.sleep(4)

def scrape():
    browser = init_browser()


#Visit the URL
Nasa_news_url = 'https://mars.nasa.gov/news/'
browser.visit(Nasa_news_url)
html = browser.html

#Parse HTML with Beautiful Soup
soup_nasa = BeautifulSoup(html, 'html.parser')
type(soup_nasa)

### NASA Mars News
#<div class="content_title"><a href="/news/8782/sensors-on-mars-2020-spacecraft-answer-long-distance-call-from-earth/" target="_self">
#Sensors on Mars 2020 Spacecraft Answer Long-Distance Call From Earth</a></div>
#<div class="article_teaser_body">Instruments tailored to collect data during the descent of NASA's next rover through the Red Planet's atmosphere have been checked in flight.</div>
#news_paragraphs = soup_nasa.find_all('div', class_="article_teaser_body")[0].text

news_titles = soup_nasa.find_all('div', class_="content_title")[0].text
news_paragraphs = soup_nasa.find_all('div', class_="article_teaser_body")[0].text

print(news_titles) 
print ('------------------')
print(news_paragraphs) 

### JPL Mars Space Images - Featured Image
url= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
time.sleep(5)
#print(soup.prettify())

#go to the full image
#data-fancybox-href
image = browser.find_by_id('full_image')
image.click()
time.sleep(5)
browser.click_link_by_partial_text('more info')

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

url_image_find = soup.find('img',class_= 'main_image').get("src")

featured_image_url =  'https://www.jpl.nasa.gov' + url_image_find
featured_image_url
### Mars Facts
url = 'https://space-facts.com/mars/'
mars_facts_df = pd.read_html('https://space-facts.com/mars/')[2]
mars_facts_df
mars_facts_df.columns =["Details", "Measures"]
mars_facts_df
mars_facts_df = mars_facts_df.to_html()
mars_facts_df 
### Mars Hemispheres
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
browser.visit(url)
web_links = browser.find_by_css("a.product-item h3")
len(web_links)
web_list = []
for i in range(len(web_links)):
    web_hemispheres = {}
    browser.find_by_css("a.product-item h3")[i].click()
    web_hemispheres["link"]= browser.find_link_by_text('Sample').first["href"]
    web_hemispheres["Title"]= browser.find_by_css('h2.title').text
    web_list.append(web_hemispheres)
    browser.back()
    web_list

browser.quit

scrape()
