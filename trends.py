import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
from datetime import datetime
import json
from selenium.common.exceptions import NoSuchElementException
from bson import ObjectId
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from dotenv import load_dotenv


load_dotenv()

USERNAME = os.getenv("TWITTER_USERNAME")
PASSWORD = os.getenv("TWITTER_PASSWORD")
EMAIL = os.getenv("EMAIL")
PROXY = os.getenv("PROXY")
MONGO_URI = os.getenv("MONGO_URI")

proxy_auth_plugin_path = "proxy_auth_plugin.zip"

chrome_options = Options()
chrome_options.add_extension(proxy_auth_plugin_path)

# chrome_options.add_argument(f"--proxy-server={PROXY}")

service = Service("C:\\Users\\ROHAN\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

# public IP address


def get_public_ip():
    try:
        # Make the request to ipify API to get the public IP
        response = requests.get('https://api.ipify.org?format=json', proxies={
            'http': f'{PROXY}',
            'https': f'{PROXY}'
        })
        
        ip_address = response.json().get('ip')
        
        # Print and return the IP address
        print(f"Current Public IP: {ip_address}")
        return ip_address
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP: {e}")
        return None


def fetch_trending_topics():
    driver = webdriver.Chrome()
    driver.get("https://x.com/login")
    driver.implicitly_wait(20)

    # Log in to Twitter
    username_field = WebDriverWait(driver, 20).until(
             EC.presence_of_element_located((By.NAME, "text"))
         )
    username_field.send_keys(USERNAME)
    username_field.send_keys(Keys.RETURN)

    #  delay for loading login steps
    driver.implicitly_wait(10)
    
    
    # try:
    #     email_field = WebDriverWait(driver, 20).until(
    #             EC.presence_of_element_located((By.NAME, "email"))
    #         )
    #        
    #     email_field.send_keys(EMAIL)
    #     email_field.send_keys(Keys.RETURN)
    # except NoSuchElementException:
    #     pass
    
    
    password_field = WebDriverWait(driver, 20).until(
             EC.presence_of_element_located((By.NAME, "password"))
        )
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)

    # Wait for homepage to load
    driver.implicitly_wait(20)

    # LOGIC for extracting trends

    # Locate "What’s Happening" section and fetch trending topics

    # for every div element with css selectordata-testid='trend' in div 'aria-label' with value 'Timeline: Trending now' 

    # for every div in div with css selector with data-testid ='trend' we have to target div with like

    # example- <div dir="ltr" class="css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-b88u0q r-1bymd8e" style="text-overflow: unset; color: rgb(231, 233, 234);">
    # <span class="r-18u37iz"><span dir="ltr" class="css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3" style="text-overflow: unset;">#PriyankaChopra</span></span></div>  

    #  and we have to extract the text from the span inside this each div

    trending_section = WebDriverWait( driver, 50).until( 
           EC.presence_of_element_located((By.XPATH, "//div[contains(@aria-label, 'Timeline: Trending now')]"))
        )

    # this specific CSS selector div
    trend_divs = trending_section.find_elements(By.CSS_SELECTOR, "[data-testid='trend']")

    # Extract the trending topics text
    topics = []
    for trend in trend_divs[:5]:  # first 5 topics
        try:
            span_element = trend.find_element(By.XPATH, ".//div[2]/span")
            topics.append(span_element.text)
        except NoSuchElementException:
          topics = []

 


    #  timestamp
  
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Storing data in MongoDB
    client = MongoClient(MONGO_URI)
    db = client["twitter_trends"]
    collection = db["trending"]

    record = {
        "_id": str(ObjectId()),
        "trend1": topics[0] if len(topics) > 0 else None,
        "trend2": topics[1] if len(topics) > 1 else None,
        "trend3": topics[2] if len(topics) > 2 else None,
        "trend4": topics[3] if len(topics) > 3 else None,
        "trend5": topics[4] if len(topics) > 4 else None,
        "timestamp": timestamp,
        "ip_address": get_public_ip(),
    }

    collection.insert_one(record)
 
    driver.quit()
    return record
    


if __name__ == "__main__":
    result = fetch_trending_topics()
    print(json.dumps(result, indent=4))

 