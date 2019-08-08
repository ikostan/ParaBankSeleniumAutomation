import allure
from utils.screenshot import screenshot_on_fail
from expected_results.users.john_doe import JohnDoe
from tests.context_tests.register_page_context_case import RegisterContextCase


@allure.feature("Register Page")
@allure.story('A New User Registration')
@allure.suite('Register Page Functionality')
@screenshot_on_fail()
class UserRegistrationTestCase(RegisterContextCase):

	def fill_out_user_data(self, client=JohnDoe, browser='chrome'):  # TODO: remove browser after done

		self.open_web_browser(browser)  # TODO: remove it after done

		self.page.type_first_name(client.FIRST_NAME)
		self.page.type_last_name(client.LAST_NAME)
		self.page.type_address(client.ADDRESS)
		self.page.type_city(client.CITY)
		self.page.type_state(client.STATE)
		self.page.type_zip_code(client.ZIP_CODE)
		self.page.type_phone(client.PHONE)
		self.page.type_ssn(client.SSN)

		self.page.type_username(client.USERNAME)
		self.page.type_password(client.PASSWORD)
		self.page.type_confirm(client.PASSWORD)

		import time  # TODO: remove it after done
		time.sleep(5)  # TODO: remove it after done

