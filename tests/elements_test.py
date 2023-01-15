import time

from pages.base_page import BasePage

# commit 2
def test(driver):
    page = BasePage(driver, 'https://demoqa.com/text-box')
    page.open()
    time.sleep(3)