from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest


class LifetrackerHomePageTest(unittest.TestCase):
    
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

    # Edith has heard about a life tracking app. She goes to check out its home
    # page.

    # She notices the title
    def test_title(self):
        self.browser.get('http://localhost:5000')
        self.assertIn('LifeTracker', self.browser.title)

    # There are some examples of things the lifetracker can do

    # There is a login/register doodad




if __name__ == '__main__':
    unittest.main()
