from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ExtractorService:

    def __init__(self):
        chrome_options = self.config()
        self.browser = webdriver.Chrome(executable_path="crawler/drives/chromedriver_win32/chromedriver.exe",
                                        chrome_options=chrome_options)
        # self.browser = webdriver.Chrome(executable_path="crawler/drives/chromedriver_linux64/chromedriver",
        #                                 chrome_options=chrome_options)

    def config(self):
        # Chrome Config
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        return chrome_options

    def execute(self, site):
        self.browser.get(site['link'])
        self.browser.implicitly_wait(3)

        try:
            form = self.browser.find_element(By.CSS_SELECTOR, site['selector'])
            inputs_selector = form.find_elements(By.TAG_NAME, "input")

            array_inputs_selector = []

            for e in inputs_selector:
                print(e.text)
                array_inputs_selector.append(e.text)

            form = self.browser.find_element(By.XPATH, site['xpath'])
            inputs_xpath = form.find_elements(By.TAG_NAME, "input")

            array_inputs_xpath = []

            for e in inputs_xpath:
                val = e.get_attribute("name")
                print(val)
                array_inputs_xpath.append(val)

            return {
                'error': False,
                'inputs_selector': array_inputs_selector,
                'inputs_xpath': array_inputs_xpath,
            }
        except Exception as e:
            return {
                'error': True,
                'message': str(e)
            }

    def close(self):
        self.browser.quit()
