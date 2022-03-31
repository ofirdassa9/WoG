from selenium import webdriver
import os
import sys
ip = os.environ['HOSTIP']

def test_scores_service(url):
    print("started")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url)
    print("initilazied browser")
    browser.get(url)
    print(f"got {url}")
    score = browser.find_element_by_id('score')
    print(f"the score is {score.text}")
    if 0 <= int(score.text) <= 1000:
        return True
    return False

def main_function():
    if not test_scores_service(f"http://{ip}:5000"):
        sys.exit(1)
    sys.exit(0)

main_function()