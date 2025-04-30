from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def get_windows11_iso_link():
    # Initialize the driver
    driver = webdriver.Chrome()  # You need to have chromedriver installed
    
    try:
        # Step 1: Go to the Windows 11 download page
        driver.get("https://www.microsoft.com/en-us/software-download/windows11")
        
        # Step 2: Find and select the Windows 11 multi-edition ISO option
        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "product-edition"))
        )
        select = Select(select_element)
        select.select_by_visible_text("Windows 11 (multi-edition ISO for x64 devices)")
        
        # Step 3: Click the download button
        download_button = driver.find_element(By.ID, "submit-product-edition")
        download_button.click()
        
        # Step 4: Wait for the page to load
        time.sleep(2)
        
        # Step 5: Select English (United States) from the language dropdown
        language_select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "product-languages"))
        )
        language = Select(language_select)
        language.select_by_visible_text("English (United States)")
        
        # Step 6: Click confirm
        confirm_button = driver.find_element(By.ID, "submit-sku")
        confirm_button.click()
        
        # Step 7: Wait for the page to load
        time.sleep(2)
        
        # Step 8: Grab the 64-bit download link
        download_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.button-flat.button-primary"))
        )
        
        # Step 9: Return the link
        return download_link.get_attribute('href')
        
    finally:
        driver.quit()

# Get and print the download link
if __name__ == "__main__":
    iso_link = get_windows11_iso_link()
    print(f"Windows 11 ISO download link: {iso_link}")
