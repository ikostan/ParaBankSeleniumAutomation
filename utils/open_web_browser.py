#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from utils.driver import Driver
from utils.refresh_page import refresh_page
from utils.http_status_code import get_http_status_code


def open_web_browser(browser: str, page_model, page_context):
	'''
	Take care of following procedure:
		1. Instantiate Selenium webdriver
		2. Instantiate Page Model Object
		3. Checks HTTP status code
		4. Open web browser > open test web page
		5. Refresh web browser in case test web site is not loaded
		6. Returns page instance (Page Model Object)
	:param browser:
	:param page_model:
	:param page_context:
	:return:
	'''

	# Open web page
	with allure.step("Open following web page: {}.".format(page_context.URL)):
		driver = Driver(browser, is_debug=True)
		page = page_model(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
		get_http_status_code(page_context.URL)
		page.go()
		refresh_page(page_context.TITLE, page)
		return page
