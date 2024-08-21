from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re

chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode
# chrome_options.add_argument("--disable-gpu")  # Recommended for headless mode
# chrome_options.add_argument("--window-size=1920,1080")  # Set a default window size
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

url = "https://www.collegpt.com/sem_7_3_units"
print("Downloading Web driver for chrome...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'box'))
)

box_links = driver.find_elements(By.CLASS_NAME, 'box')

for link in box_links:
    branch_name = link.text.strip()
    branch_url = link.get_attribute('href')
    print(f"Downloading: pdf for chapter **{branch_name}**")

    driver.execute_script("window.open(arguments[0]);", branch_url)
    driver.switch_to.window(driver.window_handles[-1])
    
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'rounded-3xl'))
        )
        src_url = element.get_attribute('src')
        
        if src_url:
            match = re.search(r'/d/([a-zA-Z0-9_-]+)', src_url)
            if match:
                file_id = match.group(1)
                download_url = f'https://drive.usercontent.google.com/uc?id={file_id}&export=download'
                driver.get(download_url)
    
    except Exception as e:
        print()
    finally:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

driver.quit()