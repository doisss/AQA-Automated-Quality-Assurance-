from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.devtools.v136.fed_cm import click_dialog_button

browser = webdriver.Chrome()
browser.get('https://www.qa-practice.com/elements/button/simple')
#click_button = browser.find_element(By.ID, 'submit-id-submit')
#click_button.click()

#click_button2 = browser.find_element(By.CLASS_NAME, 'btn')
#click_button2.click()

#click_button3 = browser.find_element(By.CSS_SELECTOR, 'input[class="btn btn-primary"]')
#click_button3.click()

#browser.find_element(By.LINK_TEXT, 'Contact').click()

click_button4 = browser.find_element(By.XPATH, '//input[@class="btn btn-primary"]')
click_button4.click()