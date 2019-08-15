#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import time
import allure

from utils.open_web_browser import open_web_browser

from page_object_models.register_page_model import RegisterPageModel
from expected_results.page_content.register_page_content import RegisterPageContent


def register_user(user):
	'''
	Registers a new user.
	Does not check for any errors.
	Using Selenium webdriver + chrome browser by default
	:param page:
	:param user:
	:return:
	'''

	page_model = RegisterPageModel
	page_context = RegisterPageContent
	browser = 'chrome'

	print("\nOpen web browser")
	page = open_web_browser(browser=browser,
	                        page_model=page_model,
	                        page_content=page_context)

	with allure.step("Fill out Register web form"):
		print("\nFilling out user data...")
		page.type_first_name(user.first_name)

		page.type_last_name(user.last_name)

		page.type_address(user.address)

		page.type_city(user.city)

		page.type_state(user.state)

		page.type_zip_code(user.zip_code)

		page.type_phone(user.phone)

		page.type_ssn(user.ssn)

		page.type_username(user.username)

		page.type_password(user.password)

		page.type_confirm(user.password)

	with allure.step("Hit 'REGISTER' button"):
		page.click_register_btn()
		time.sleep(3)

	with allure.step("Do Log Out"):
		page.hit_log_out_button()
		time.sleep(3)

	with allure.step("Close web browser"):
		page.quit()
