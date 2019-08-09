import time


def clean_database(page):
	'''
	Clean and initialise database.
	Does not check for any errors.
	:return:
	'''

	page.hit_clean_button()

	time.sleep(3)
	
	page.hit_initialize_button()
