from pages.base_page import BasePage
import time


def test_example(driver):
    page = BasePage(driver, "google.com")
    page.open()
    time.sleep(3)



