from sys import platform as _platform
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class Test():

    driver = None


    def __init__(self, site_path=None, login = "dnk131", password = "1pt7ebcH"):
        self.login = login
        self.password = password
        self.get_driver()
        if site_path is None:
            self.site_path = "https://dnkteam.clientbase.ru/login.php"
        else:
             self.site_path = site_path
    

    def run_tests(self):
        self.auth()
        self.create_note()
        time.sleep(10)
        self.driver.close()
        

    def auth(self):
        driver = self.driver
        driver.get(self.site_path)
        login_field = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath('//*[@id="all_nonmenu_text"]/div/form/div/div/div/div[1]/input'))
        login_field.send_keys(self.login)
        pass_field = driver.find_element_by_xpath('//*[@id="all_nonmenu_text"]/div/form/div/div/div/div[2]/input')
        pass_field.send_keys(self.password)
        button_enter = driver.find_element_by_xpath('//*[@id="all_nonmenu_text"]/div/form/div/div/div/div[4]/div/div/input[1]')
        button_enter.click()


    def create_note(self):
        driver = self.driver
        driver.get("https://dnkteam.clientbase.ru/view_line2.php?table=120&filter=180&line=new")
        title_field = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath('//*[@id="value1590"]'))
        title_field.send_keys("Test")
        text_field = driver.find_element_by_xpath('//*[@id="field_edit1600_td1"]/div/div[3]/div[2]')
        text_field.send_keys("Test")
        button_submite = driver.find_element_by_xpath('//*[@id="edit_buttons"]/div/div/button[1]')
        button_submite.click()      


    def get_driver(self):
         # Linux x64
        if _platform == "linux" :
            self.driver = webdriver.Chrome("./src/drivers/linux/chromedriver")
        # MAC OS X
        elif _platform == "darwin":
            self.driver = webdriver.Chrome("./src/drivers/macos/chromedriver")
        # Windows x64
        elif _platform == "win32" or _platform == "win64":
            self.driver = webdriver.Chrome("./src/drivers/windows/chromedriver.exe")

