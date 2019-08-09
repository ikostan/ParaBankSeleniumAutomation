import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_locators.home_page_locator import HomePageLocator
from tests.context_cases.home_page_context_case import HomePageContextCase
from expected_results.page_context.home_page_context import HomePageContext


class UserLogin(HomePageContextCase):

	def register_new_user(self, client):  # TODO: remove browser after done

		with allure.step('Type username'):
			expected = client.USERNAME
			self.page.type_username(expected)
			actual = self.page.username
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type username\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))

		with allure.step('Type password'):
			expected = client.PASSWORD
			self.page.type_password(expected)
			actual = self.page.password
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Type password\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))

		import time  # TODO: remove it after done
		time.sleep(5)  # TODO: remove it after done

		with allure.step('Hit "Register" button'):
			self.page.click_register_btn()

		with allure.step('Wait for "Welcome" message'):
			WebDriverWait(self.page.driver,
			              self.page.explicit_wait_time).until(EC.presence_of_element_located(RegisterPageLocator.HEADER))

		with allure.step('Verify "Welcome" header'):
			expected = RegisterPageContext.WELCOME_MESSAGE['header'] + client.USERNAME
			actual = self.page.welcome_header
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Verify "Welcome" header\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))

		with allure.step('Verify "Welcome" message'):
			expected = RegisterPageContext.WELCOME_MESSAGE['message']
			actual = self.page.welcome_message
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Verify "Welcome" header\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))

		time.sleep(5)  # TODO: remove it after done
