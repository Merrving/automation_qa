import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# proba init commit
# proba init commit
@pytest.fixture(scope='function')

def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()