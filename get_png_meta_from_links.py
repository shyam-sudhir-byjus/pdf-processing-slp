from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
text_file = "./data_respaper_text_links/cbse-respaper-12.txt"

url = os.environ.get('URL_RESPAPER')
user_name = os.environ.get('USERNAME_RESPAPER')
password = os.environ.get('PASSWORD_RESPAPER')

driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

'''
    Login to Respaper Website
'''
driver.find_element(By.XPATH, "//input[@id='ui']").send_keys(user_name)
driver.find_element(By.XPATH, "//input[@id='pw']").send_keys(password)
driver.find_element(By.XPATH, "//input[@value='Sign in']").click()
time.sleep(1)

with open(text_file,"r") as f:
    urls = f.readlines()

urls = [url.replace("\n","") for url in urls]

paper_count = 0
page_count = 0

for idx, url in enumerate(urls):
    if 'NEXT' in url:
        paper_count += 1
        page_count = 1
        driver.get(urls[idx+1].split('?')[0])
        file_name = driver.find_element(By.XPATH, '//h1').text
        continue

    if url == '':
        continue

    # driver.get("https://www.respaper.com/")
    driver.get(url)
    screenshot_file = f'./respaper_cbse_12_pngs/cbse_12_{file_name}_{paper_count}_{page_count}.png'
    page_count += 1
    driver.get_screenshot_as_file(screenshot_file)
    # driver.find_element_by_tag_name('body').screenshot('LambdaTestFullPage.png')

# ob = Screenshot.Screenshot() 
# driver.get("https://www.respaper.com/9938480846/273/4149-pdf.html?cmd=get_page&pn=3")
# img_url=ob.full_Screenshot(driver, save_path=r'.', image_name='google.png') 
# # screenshot_file = "dsd1sd.png"
# driver.get_screenshot_as_file(screenshot_file)