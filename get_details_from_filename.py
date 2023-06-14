from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import ActionChains 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
import time

options = webdriver.ChromeOptions()

options.add_experimental_option('prefs',{
    "download.default_directory" : "/Users/tnluser/Documents/chatgpt_question_answer/data_respaper/icse",
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True
})

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

text_file = "./data_respaper_gifs/icse-respaper-9.txt"

with open(text_file,"r") as f:
    urls = f.readlines()

urls = [url.replace("\n","") for url in urls]
urls = [url.split('?')[0] for url in urls]
urls = list(set(urls))[1:]

paper_names = []

for url in urls:
    driver.get(url)
    paper_name = driver.find_element(By.XPATH, '//h1').text
    paper_names.append(paper_name)

paper_names
            