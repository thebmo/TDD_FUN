from selenium import webdriver

browser = webdriver.Firefox()

# This dude is like "wow, have you seen this kitten video yet?
# He loads up the site.
browser.get('http://localhost:8000')

# The title reads 'to-do leests'
assert 'Django' in browser.title

# There are no kittens here but rather a blank list of items to do

# The adds 'check out that sweet kitten vid' to the list

# There is still more room for items, so he adds 'google pug pictures'

# After the page refreshes, both items are on the list

# There is a special URL that gives the dude access to his link

# The dude verifies the URL works

# The dude closes his browser

browser.quit()