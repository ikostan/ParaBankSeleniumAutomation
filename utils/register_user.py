#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import time
from utils.http_status_code import get_http_status_code
from utils.open_web_browser import open_web_browser
from page_models.register_page_model import RegisterPageModel
from expected_results.page_context.register_page_context import RegisterPageContext


def register_user(client):
	'''
	Register a new user.
	Does not check for any errors.
	:param page:
	:param client:
	:return:
	'''

	page_model = RegisterPageModel
	page_context = RegisterPageContext
	browser = 'chrome'

	print("Open web browser")
	get_http_status_code(RegisterPageContext.URL)
	page = open_web_browser(browser=browser,
	                        page_model=page_model,
	                        page_context=page_context)

	print("Filling out user data...")
	page.type_first_name(client.FIRST_NAME)

	page.type_last_name(client.LAST_NAME)

	page.type_address(client.ADDRESS)

	page.type_city(client.CITY)

	page.type_state(client.STATE)

	page.type_zip_code(client.ZIP_CODE)

	page.type_phone(client.PHONE)

	page.type_ssn(client.SSN)

	page.type_username(client.USERNAME)

	page.type_password(client.PASSWORD)

	page.type_confirm(client.PASSWORD)

	print("Clicking on Register button")
	page.click_register_btn()
	time.sleep(3)

	print("Log out")
	page.log_out()
	time.sleep(3)

	print("\nClose web browser")
	page.quit()
