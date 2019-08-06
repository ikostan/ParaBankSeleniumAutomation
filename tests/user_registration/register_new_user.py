from expected_results.users.john_doe import JohnDoe
from tests.context_tests.register_context_case import RegisterContextTestCase


class UserRegistratironTestCase(RegisterContextTestCase):

	def test_fill_out_user_data(self, browser = 'chrome'):

		self.open_web_browser(browser)  # TODO: remove it after done

		self.page.type_first_name(JohnDoe.FIRST_NAME)
		self.page.type_last_name(JohnDoe.LAST_NAME)
		self.page.type_address(JohnDoe.ADDRESS)
		self.page.type_city(JohnDoe.CITY)
		self.page.type_state(JohnDoe.STATE)
		self.page.type_zip_code(JohnDoe.ZIP_CODE)
		self.page.type_phone(JohnDoe.PHONE)
		self.page.type_ssn(JohnDoe.SSN)

		self.page.type_username(JohnDoe.USERNAME)
		self.page.type_password(JohnDoe.PASSWORD)
		self.page.type_confirm(JohnDoe.PASSWORD)

		import time  # TODO: remove it after done
		time.sleep(5)  # TODO: remove it after done

