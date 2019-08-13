#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import time
from utils.open_web_browser import open_web_browser

from page_object_models.register_page_model import RegisterPageModel
from expected_results.page_content.register_page_content import RegisterPageContent


def register_user(client):
	'''
	Registers a new user.
	Does not check for any errors.
	Using Selenium webdriver + chrome browser by default
	:param page:
	:param client:
	:return:
	'''

	page_model = RegisterPageModel
	page_context = RegisterPageContent
	browser = 'chrome'

	print("Open web browser")
	page = open_web_browser(browser=browser,
	                        page_model=page_model,
	                        page_content=page_context)

	print("Filling out user data...")
	page.type_first_name(client.first_name)

	page.type_last_name(client.last_name)

	page.type_address(client.address)

	page.type_city(client.city)

	page.type_state(client.state)

	page.type_zip_code(client.zip_code)

	page.type_phone(client.phone)

	page.type_ssn(client.ssn)

	page.type_username(client.username)

	page.type_password(client.password)

	page.type_confirm(client.password)

	print("Clicking on Register button")
	page.click_register_btn()
	time.sleep(3)

	print("Log out")
	page.log_out()
	time.sleep(3)

	print("\nClose web browser")
	page.quit()
