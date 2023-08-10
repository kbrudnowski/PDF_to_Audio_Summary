from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class Summarizer:
    def __init__(self, text_input):
        self.service = Service("../Development/chromedriver.exe")
        self.options = Options()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(service = self.service, options = self.options)

        self.driver.get("https://www.summarizer.org/")

        consent_btn = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[1]/div[3]/div[2]/button[1]/p')
        consent_btn.click()

        input_textarea = self.driver.find_element(By.ID, 'input_text')
        input_textarea.send_keys(text_input)

        submit_btn = self.driver.find_element(By.ID, 'tool-submit-btn')
        submit_btn.click()

        time.sleep(1)

        self.summarized_text = self.driver.find_element(By.ID, 'output-summary-content').text
