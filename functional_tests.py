import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # This dude is like "wow, have you seen this kitten video yet?
        # He loads up the site.
        self.browser.get('http://localhost:8000')

        # The title reads 'to-do leests'
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # There are no kittens here but rather a blank list of items to do

        # The adds 'check out that sweet kitten vid' to the list

        # There is still more room for items, so he adds 'google pug pictures'

        # After the page refreshes, both items are on the list

        # There is a special URL that gives the dude access to his link

        # The dude verifies the URL works

        # The dude closes his browser
        

if __name__ == '__main__':
    unittest.main()
