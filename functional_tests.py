from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest


class FlaskAppTest(unittest.TestCase):
    
    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        '''
        chrome_options.add_argument('--remote-debugging-port=9222')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        '''

        self.browser = webdriver.Chrome('/opt/WebDriver/bin/chromedriver', options=chrome_options)

    def tearDown(self):
        time.sleep(1)
        self.browser.quit()

    def test_app_works(self):
        self.browser.get('http://localhost:5000')
        self.assertIn('flask app', self.browser.page_source)


if __name__ == '__main__':
    unittest.main()
