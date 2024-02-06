import time
import re
import math
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up the WebDriver
driver = webdriver.Chrome()

# Set the URL of the first page
homeopathy_url = 'https://www.1mg.com/categories/homeopathy-57?filter=true&pageNumber=1'
driver.get(url=homeopathy_url)

# Remove dropdown popup
try:
    close_popup_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'UpdateCityModal__cancel-btn___2jWwS'))
    )
    close_popup_button.click()
except Exception as e:
    print(f"Error closing popup: {e}")

# Create empty lists to store data
Name = []
Size = []
MRP_Price= []
Sale = []
Link = []

# Making soup
soup = BeautifulSoup(driver.page_source, "html.parser")

total_number_of_pages = 250
medicines_per_page = 40

# Get user input for the desired number of medicines
desired_medicines = int(input(f"How many medicines' details do you want (max {total_number_of_pages * medicines_per_page})? "))

# Calculate the number of pages needed
pages_needed = math.ceil(desired_medicines / medicines_per_page)

# Iterate through the pages
for page_number in range(1, pages_needed + 1):
    homeopathy_url = f'https://www.1mg.com/categories/homeopathy-57?filter=true&pageNumber={page_number}'
    driver.get(url=homeopathy_url)

    # Wait for some time to ensure the page is fully loaded
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'style__product-box___liepi'))
    )

    # Making soup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    blocks = soup.find_all("div", {"class": "style__product-box___liepi"})

    for i in blocks:

        name_of_medicine = i.find('div', {'class': 'style__pro-title___2QwJy'}).text
        print(name_of_medicine)

        size_text = i.find('div', {'class': 'style__pack-size___2JQG7'}).text
        # Define a regular expression to extract the volume information
        volume_pattern = re.compile(r'\b(\d+\s*(?:ml|gm|tablets))\b', re.IGNORECASE)
        # Find all matches in the text
        matches = volume_pattern.findall(size_text)
        # Print the volumes
        for size in matches:
            print(size)


        MRP_element = i.find("span", {"class": "style__discount-price___25Bya"})
        if MRP_element:
            MRP = MRP_element.text.strip()
            print(MRP)
        else:
            print("NA")

        sale_price_element = i.find("div", {"class": "style__price-tag___cOxYc"})
        if sale_price_element:
            sale_price = sale_price_element.text.strip()
            print(sale_price)
        else:
            print("NA")

        url_element = i.find('a', {'class': 'style__product-link___UB_67'})
        url = f'https://www.1mg.com{url_element.get("href")}'
        print(url)

        Name.append(name_of_medicine)
        Size.append(size)
        MRP_Price.append(MRP)
        Sale.append(sale_price)
        Link.append(url)

    # print(len(blocks))
# Create a DataFrame
data = {
    'Name': Name,
    'Size': Size,
    'MRP': MRP_Price,
    'Sale Price':Sale ,
    'URL': Link
}

df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('rough.csv', index=True)

# Close the WebDriver
driver.quit()

