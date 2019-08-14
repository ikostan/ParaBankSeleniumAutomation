#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import time


def refresh_page(expected, page, sleep_time=3):
	'''
	1. Check if page has expected title.
	2. Trying to refresh web page in case page title dos not equal expected result
	3. Raises exception in case page title dos not equal expected result

	:param expected:
	:param sleep_time:
	:param page:
	:return:
	'''

	counter = 0
	while expected != page.title() and counter < 5:
		print("\nERROR: expected page title {} != {}.\nTrying to refresh...\n".format(expected, page.title()))
		page.driver.refresh()
		counter += 1
		time.sleep(sleep_time)

	if expected != page.title():
		raise Exception("\nERROR: This site can't be reached\n")

	return None
