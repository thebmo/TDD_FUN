import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIN('To-Do', header_text)

        # There are no kittens here but rather a blank list of items to do
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )

        # The adds 'check out that sweet kitten vid' to the list
        inputbox.send_keys('check out that sweet kitten vid')
        inputbox.send_keys(Keys.ENTER)

        table = self.browswer.find_element_by_id('id_list_table')
        rows = table.find_elemebt_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: check out that sweet kitten vid' for row in rows)
            )
        
        # There is still more room for items, so he adds 'google pug pictures'
        self.fail('FINISH THE TEST')
        

        # After the page refreshes, both items are on the list

        # There is a special URL that gives the dude access to his link

        # The dude verifies the URL works

        # The dude closes his browser
        

if __name__ == '__main__':
    unittest.main()
