from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# changes if you needed
COMMENTS = [
    "super", "amazing one", "what a acting", "great video", "have a nice day",
    "keep going", "keep rocking", "all the best buddy", "next video please",
    "one of the best video everseen", "wonderful day", "great one seen today",
    "superb", "magnifying", "shared to my friends", "best thing in internet",
    "sensational video", "dashing", "marvelous", "next big video in internet",
    "always good content hits", "people will really liked these video", "good food have humans good",
    "all the best dude"
]
VIDEO_URL = "https://www.youtube.com/watch?v=jNQXAC9IVRw&ab_channel=jawed" #replace with required
COMMENTS_PER_ACCOUNT = 50 #No of Comments per acc (no 50+)
NUM_ACCOUNTS = 10 #replace how much accs want (no 10 more accs)


option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=option)

#pause the video
def pause_video():
    try:
        pause_button = driver.find_element(By.CSS_SELECTOR, '#movie_player .ytp-left-controls button') #pause the youtube video
        pause_button.click()
    except NoSuchElementException:
        print("Pause button not found.")
    time.sleep(2)

def scroll_down():
    driver.execute_script("window.scrollTo(0, 600);")
    time.sleep(1)
    
    
#comments
def post_comment(comment):
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))
        comment_box = driver.find_element(By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer div#placeholder-area")
        comment_box.click()
        content_editable = driver.find_element(By.CSS_SELECTOR, "#contenteditable-root")
        content_editable.send_keys(comment)
        time.sleep(2)
        submit_button = driver.find_element(By.ID, "submit-button")
        submit_button.click()
        time.sleep(4)
    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error posting comment: {e}")

#switch acc..
def switch_account(account_index):
    try:
        driver.find_element(By.ID, "avatar-btn").click() #click on acc 
        time.sleep(3)
        driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()') #click on switch acc 
        time.sleep(3)
        account_selector = f'/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[{account_index+1}]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div'
        driver.find_element(By.XPATH, account_selector).click()
        time.sleep(7)
    except NoSuchElementException as e:
        print(f"Error switching account: {e}")

def main():
    driver.get(VIDEO_URL)
    time.sleep(6)
    pause_video()
    scroll_down()

    for account_index in range(NUM_ACCOUNTS):
        counter = 0
        while counter < COMMENTS_PER_ACCOUNT:
            comment = random.choice(COMMENTS)
            post_comment(comment)
            counter += 1

        if account_index < NUM_ACCOUNTS - 1:
            switch_account(account_index + 1)
            pause_video()
            scroll_down()

    driver.quit()

if __name__ == "__main__":
    main()
