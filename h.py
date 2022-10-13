#cd C:\Users\Hp\AppData\Local\Google\Chrome\Application

#chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\Hp\Desktop\Bots\Chromedriver\Localhost"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

comments = ["super","amazing one","what a acting","great video","have a nice day","keep going","keep rocking","all the best buddy","next video please","one of the best video everseen","wonderful day","great one seen today","superb","magnifying","shared to my friends","best thing in internet","sensational video",
"dashing","marvelous","next big video in internet","always good content hits","people will really liked these video","good food have humans good","all the best dude",] #change comments if you needed your wish comments means

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")

driver = webdriver.Chrome(options=option)

driver.get("https://www.youtube.com/watch?v=dOKQeqGNJwY") #replace with your url

time.sleep(7)

driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

time.sleep(3)

driver.execute_script("window.scrollTo(0, 600);")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("dboss")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

driver.close()