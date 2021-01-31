

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



html=browser.html
new_soup=soup(html, 'html.parser')
slide_elem=new_soup.select_one('ul.item_list li.slide')



slide_elem.find("div", class_='content_title')



# USe the parent element to find the first 'a' tag and save it as 'news_title' 
news_title=slide_elem.find("div", class_='content_title').get_text()
news_title



# Use the parent element to find the paragraph text
news_p=slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

 ### Featured Images

# Visit URL
url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


browser.links.find_by_partial_text("Mars Probe Landing Ellipses").click()


browser.links.find_by_partial_text("Download JPG").click()



# Find and click the full image button
html=browser.html
full_image_elem=soup(html, "html.parser")
full_image=full_image_elem.find('img')
print(full_image["src"])


# Use 'read_html' to scrape the facts table into a dataframe
df=pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df



df.to_html()


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)



# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())



# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)



# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []



# 3. Write code to retrieve the image urls and titles for each hemisphere.
 h=browser.find_link_by_partial_text("Hemisphere Enhanced")

    for i in range (len(h)):
        browser.links.find_by_partial_text("Hemisphere Enhanced")[i].click()
        html=browser.html
        info={}
        soup_info=soup(html, "html.parser")
        title=soup_info.find("h2", class_="title").get_text()
        info["title"]=title
        image=soup_info.find_all("a")[4]["href"]
        info["img_url"]=image
        hemisphere_image_urls.append(info)
        browser.back()
    #Return scrapped data as list of dictionaries with url string and title
    print(hemisphere_image_urls)
    



# 5. Quit the browser
browser.quit()




