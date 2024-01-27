from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def test_setup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Test Completed")

def test_login( test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # driver.implicitly_wait(15)
    driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
    driver.find_element(By.XPATH ,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys( "admin123")
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

def test_logout(test_setup):
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()


