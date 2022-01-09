from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
user = ["username or list for sending message"]


class WhatsAppBot:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--disable-extensions")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--user-data-dir=./User_Data')
        self.options.add_argument("--test-type")
        self.driver = webdriver.Chrome(options=self.options, executable_path="path to selenium webdriver")
        self.driver.get('https://web.whatsapp.com')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.user = user
        time.sleep(5)

    def find_user_and_send_message(self):
        for user_ in self.user:
            try:
                search_user = self.driver.find_element_by_css_selector('div[role="textbox"]')
                search_user.send_keys(user_)
                search_user.send_keys(Keys.ARROW_DOWN)
                search_user.send_keys(Keys.RETURN)
                message = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
                message.send_keys("Send mains test portions")
                message.send_keys(Keys.RETURN)
            except Exception:
                print("the user is not in the contacts")


if __name__ == '__main__':
    bot = WhatsAppBot()
    bot.find_user_and_send_message()
