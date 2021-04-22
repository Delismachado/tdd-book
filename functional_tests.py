from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def setDown(self):
        self.browser.quit

    def test_can_start_a_list_and_retrieve_it_later(self):
        # I hed heard about a cool new online to-do app. I go to see
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        #I noticed the page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # I is invite to enter a to-do item straight away
        # I types "Buy pizza for dinner" into a text box 

        # When i hits enter, the page updates, ans now the page list
        # "1: Buy pizza for dinner" as an item in a to-do list

        # There is still a test box inviting me to ass another item; I
        # enters "Comer pizza às 19h"

        # The page updates again, and now shoes both items on my list
        # I wonders whether the site will remember my list. Them i sees
        # that the site has generated a unique URL for me -- there is some
        # explantory test to that effect.

        # I visits that URL - my to-do list is still there.

        # Satisfied, i goes back to sleep.

        browser.quit()
if __name__ == '__main__':
    unittest.main()