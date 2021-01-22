# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set the executable path and initialize the chrome browser in splinter
executable_path={'executable_path': ChromeDriverManager().install()}
browser=Browser('chrome', **executable_path, headless= False)


# Visit the mars nasa news site
url='https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

#Convert the browser html to a soup object and then quit browser
html=browser.html
new_soup=soup(html, 'html.parser')

slide_elem=new_soup.select_one('ul.item_list li.slide')
slide_elem.find("div", class_='content_title')


# USe the parent element to find the first 'a' tag and save it as 'news_title' 
new_title=slide_elem.find("div", class_='content_title').get_text()
new_title

# Use the parent element to find the paragraph text
news_p=slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

# Visit URL
url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# Find and click the full image button
full_image_elem=browser.find_by_id('full_image')
full_image_elem.click()

# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem=browser.links.find_by_partial_text('more info')
more_info_elem.click()

df=pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df

df.to_html()

browser.quit()





