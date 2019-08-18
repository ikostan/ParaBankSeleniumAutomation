#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from utils.driver import Driver
from utils.refresh_page import refresh_page
from utils.http_status_code import get_http_status_code


def open_web_browser(page_model, page_content):
	'''
	Take care of following procedure:
		1. Instantiate Selenium webdriver
		2. Instantiate Page Model Object
		3. Checks HTTP status code
		4. Open web browser > open test web page
		5. Refresh web browser in case test web site is not loaded
		6. Returns page instance (Page Model Object)
	:param page_model:
	:param page_content:
	:return:
	'''

	# Open web page
	with allure.step("Open following web page: {}.".format(page_content.URL)):
		driver = Driver(is_debug=True)
		page = page_model(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
		get_http_status_code(page_content.URL)
		page.go()
		refresh_page(page_content.TITLE, page)
		return page
