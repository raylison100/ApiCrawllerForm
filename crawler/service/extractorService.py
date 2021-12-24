from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class ExtractorService:

    def __init__(self):
        chrome_options = self.config()
        self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def config(self):
        # Chrome Config
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        return chrome_options

    def execute(self, site):
        self.browser.get(site['link'])
        self.browser.implicitly_wait(3)

        try:
            array_inputs_selector = []
            array_label_selector = []

            if site['selector']:
                form = self.browser.find_element(By.CSS_SELECTOR, site['selector'])
                inputs_selector = form.find_elements(By.TAG_NAME, "input")

                for e in inputs_selector:
                    val = e.text
                    if val:
                        array_inputs_selector.append(val)

                label_selector = form.find_elements(By.TAG_NAME, "label")

                for e in label_selector:
                    attr = e.get_attribute("name")

                    if attr:
                        array_label_selector.append(attr)

                    text = e.text

                    if text:
                        array_label_selector.append(text)

            array_inputs_xpath = []
            array_label_xpath = []

            if site['xpath']:
                form = self.browser.find_element(By.XPATH, site['xpath'])
                inputs_xpath = form.find_elements(By.TAG_NAME, "input")

                for e in inputs_xpath:
                    attr = e.get_attribute("name")

                    if attr:
                        array_inputs_xpath.append(attr)

                    text = e.text

                    if text:
                        array_inputs_xpath.append(text)

                label_xpath = form.find_elements(By.TAG_NAME, "label")

                for e in label_xpath:
                    attr = e.get_attribute("name")
                    print(attr)
                    if attr:
                        array_label_xpath.append(attr)

            return {
                'error': False,
                'inputs_selector': array_inputs_selector,
                'label_selector': array_label_selector,
                'inputs_xpath': array_inputs_xpath,
                'label_xpath': array_label_xpath,
            }
        except Exception as e:
            print('----------------------------------------------------------------------')
            print('----------------------------------------------------------------------')
            print(str(e))
            print('----------------------------------------------------------------------')
            print('----------------------------------------------------------------------')
            return {
                'error': True,
                'message': str(e)
            }

    def close(self):
        self.browser.quit()
