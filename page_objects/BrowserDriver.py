import os.path
from page_objects.logger import Logger
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options

logger = Logger(logger = "BrowserDriver").getlog()

class BrowserDriver(object):

    def __init__(self, driver):
        self.driver = driver


    def browser(self, driver):
        """
        Define global browser driver
        :return:
        """
        if driver == "chrome":
            driver = webdriver.Chrome()
            driver.maximize_window()
            logger.info("启动chrome浏览器")

        elif driver == "firefox":
            driver = webdriver.Firefox()
            driver.maximize_window()
            logger.info("启动firefox浏览器")

        elif driver == "IE":
            driver = webdriver.Ie()
            driver.maximize_window()
            logger.info("启动IE浏览器")

        elif driver == "chrome-headless":
            chrome_options = CH_Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920x1080")
            driver = webdriver.Chrome(chrome_options=chrome_options)
            logger.info("启动Chrome headless浏览器")

        elif driver == "firefox-headless":
            firefox_options = FF_Options()
            firefox_options.headless = True
            driver = webdriver.Firefox(firefox_options=firefox_options)

        elif driver == "grid":
            #Remote selenium grid
            driver = Remote(command_executor='http://10.12.16.118:4444/wd/hub', desired_capabilities={
                "browserName": "chrome",
            })
            driver.maximize_window()

        else:
            raise NameError("driver驱动类型定义错误！")


        driver.implicitly_wait(5)
        logger.info("设置5秒隐式等待")
        return driver

    def browser_close(self):
        logger.info("关闭浏览器")
        self.driver.quit()