from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ExtractorService:

    def __init__(self):
        chrome_options = self.config()
        self.browser = webdriver.Chrome(executable_path="crawler/drives/chromedriver_win32/chromedriver.exe",
                                        chrome_options=chrome_options)

    def config(self):
        # Chrome Config
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        return chrome_options

    def execute(self, link, selector):
        self.browser.get(link)
        self.browser.implicitly_wait(3)

        try:
            form = self.browser.find_element(By.CSS_SELECTOR, selector)

            inputs = form.find_elements(By.TAG_NAME, "label")

            array_inputs = []

            for e in inputs:
                print(e.text)

                # val = e.get_attribute("name")
                array_inputs.append(e.text)

            return array_inputs
        except:
            return []

    def close(self):
        self.browser.quit()
