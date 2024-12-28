import random
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


# Configure ProxyMesh and Selenium

PROXY = "http://rohan11:rohan11@us-ca.proxymesh.com:31280"

chrome_options = Options()
chrome_options.add_argument(f"--proxy-server={PROXY}")

service = Service("C:\\Users\\ROHAN\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_address = response.json().get('ip')
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
    username_field.send_keys("rohann134")
    username_field.send_keys(Keys.RETURN)

    # Add a delay for loading login steps, if needed
    driver.implicitly_wait(10)

    password_field = WebDriverWait(driver, 20).until(
             EC.presence_of_element_located((By.NAME, "password"))
        )
    password_field.send_keys("Rohan@1102")
    password_field.send_keys(Keys.RETURN)

    # Wait for homepage to load
    driver.implicitly_wait(20)

# Locate "What’s Happening" section and fetch trending topics
    #  for every div element with css selectordata-testid='trend' in div 'aria-label' with value 'Timeline: Trending now' 
    #  trending_section = driver.find_element(By.CSS_SELECTOR, "[data-testid='trend']")
    #  for every div in div with css selector with data-testid ='trend' we have to target div with <div dir="ltr" class="css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-b88u0q r-1bymd8e" style="text-overflow: unset; color: rgb(231, 233, 234);"><span class="r-18u37iz"><span dir="ltr" class="css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3" style="text-overflow: unset;">#PriyankaChopra</span></span></div> this div 
    #  and we have to extract the text from the span inside each div
    trending_section = WebDriverWait( driver, 50).until( 
           EC.presence_of_element_located((By.XPATH, "//div[contains(@aria-label, 'Timeline: Trending now')]"))
        )

    # Find all elements with the specific CSS selector for trends
    trend_divs = trending_section.find_elements(By.CSS_SELECTOR, "[data-testid='trend']")

    # Extract the trending topics text
    topics = []
    for trend in trend_divs[:5]:  # Limit to the first 5 topics
        try:
            span_element = trend.find_element(By.XPATH, ".//div[2]/span")
            topics.append(span_element.text)
        except NoSuchElementException:
          topics = []

    print("Trending Topics:", topics)




    # Fetch IP address used (simulated here)
    # ip_address = PROXY.split("@")[1].split(":")[0]

    # Unique ID and timestamp
    # unique_id = str(uuid.uuid4())
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Store data in MongoDB
    client = MongoClient("mongodb+srv://admin:admin123@cluster0.nbjwb.mongodb.net/stir?retryWrites=true&w=majority&appName=Cluster0")
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

    # print(json.dumps(result,ensure_ascii=False, indent=4))
