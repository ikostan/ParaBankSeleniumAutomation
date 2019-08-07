import time


def refresh_page(title, page):
	'''
	1. Check if page has expected title.
	2. Trying to refresh web page in case page title dos not equal expected result
	3. Raises exception in case page title dos not equal expected result

	:param title:
	:param page:
	:return:
	'''

	counter = 0
	while title != page.title and counter < 5:
		print("\nERROR: expected page title {} != {}.\nTrying to refresh...\n".format(title, page.title))
		page.driver.refresh()
		counter += 1
		time.sleep(3)

	if title != page.title:
		raise Exception("\nERROR: This site can't be reached\n")

	return None
