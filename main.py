import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

GOOGLE_FORM = "https://forms.gle/5ZypFTo4XbJLizabA"
CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(CLONE_URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Create a list of all the links on the page using a CSS Selector
all_elements_links = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_elements_links]
# print(all_links)

# Create a list of all the addresses on the page using a CSS Selector
all_address_element = soup.select(".StyledPropertyCardDataWrapper address")
all_address = [address.get_text().strip(" \n") for address in all_address_element]
# print(all_address)

# Create a list of all the prices on the page using a CSS Selector
all_prices_list = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo","").split("+")[0] for price in all_prices_list]
# print(all_prices)

# Fill in the Google Form using Selenium
driver = webdriver.Chrome()

for i in range(len(all_prices)):

    driver.get(GOOGLE_FORM)
    time.sleep(5)
    addr = all_address[i]
    pricePerMonth = all_prices[i]
    li = all_links[i]

    address = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(addr)

    price = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(pricePerMonth)

    link = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(li)

    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
