from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def scrape():
    scrape_dictionary = {}

    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

    # News
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    news = browser.html
    soup = BeautifulSoup(news, "html.parser")

    news["title"] = soup.find("div", class_ = "content_title").get_text()
    news["body"] = soup.find("div", class_ = "article_teaser_body").get_text()

    scrape_dictionary["Mars News"] = news

    # Image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    image = browser.html
    soup = BeautifulSoup(image, "html.parser")

    name_image = soup.find("article", class_ = "carousel_item")["alt"] 

    url_base = "https://www.jpl.nasa.gov"
    url_full_image = soup.find(attrs={"data-title":name_image})["data-fancybox-href"] 
    featured_image_url = url_base + url_full_image

    scrape_dictionary["Mars Featured Image"] = featured_image_url

    # Weather
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    weather = browser.html
    soup = BeautifulSoup(weather, "html.parser")

    mars_weather = soup.find("p", class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    scrape_dictionary["Mars Current Weather"] = mars_weather

    # Mars Facts
    url = "https://space-facts.com/mars/"
    browser.visit(url)
    facts = browser.html
    soup = BeautifulSoup(facts, "html.parser")

    tables_facts = pd.read_html(url)

    mars_facts = tables_facts[0]
    mars_facts.columns = ["Category", "Fact"]

    html_facts = mars_facts.to_html(header=None,index=False)
    html_facts = html_facts.replace('\n', '')

    scrape_dictionary["Mars Facts"] = html_facts\

    browser.quit()
    
    return scrape_dictionary
    

    









