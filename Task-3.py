#!/usr/bin/env python
# coding: utf-8

# In[3]:


# web scraping 
import requests
from bs4 import BeautifulSoup

# url of the web site to scrape
url=("https://www.mercedes-benz.co.in/passengercars.html?group=all&subgroup=see-all&view=BODYTYPE&gagcmid=GA_20685282646_153411963263_705630403106&gad_source=1&gclid=CjwKCAjwqf20BhBwEiwAt7dtdUxgco7A1GFEzQ0W5dY_SdmJhVQEg2N5msQd8kbJvgnrzhvQx2Z46RoCSS8QAvD_BwE&gclsrc=aw.ds")

# send a get request to the web page 
response_url=requests.get(url)

# cheeck if the response is successful
if response_url.status_code==200:
    # parse the html content of the page
    my_soup=BeautifulSoup(response_url.text,'html.parser')
    
    #extract all the text from the web page
    my_page_text=my_soup.get_text()
    
    # extract all the links from the web page
    my_links=[a['href']for a in my_soup.find_all('a', href=True)]
    
    # extract all the images from the page 
    my_images=[img['src']for img in my_soup.find_all('img', src=True)]
    
    # print all the extracted data
    print("All the text of the page :-")
    print(my_page_text)
    
    print("/nAll the LINKS :-")
    for link in my_links:
        print(link)
    
    print("/nAll the IMAGES :-")
    for image in my_images:
        print(image)
else:
    print("The website is private")
    print(f"failed to retrieve the web page. Status code: {response_url.status_code}")


# In[ ]:




