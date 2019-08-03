import allure
from utils.screenshot import screenshot_on_fail
from page_context.home_page_context import HomePageContext
from allure_commons.types import Severity
from tests.context_tests.home_page_context_case import HomePageContextTestCase


# @allure.epic("ParaBank Web App")
@allure.suite("Chrome Browser Context Testing")
@screenshot_on_fail()
class ChromeHomePageContextTestCase(HomePageContextTestCase):

	browser = 'chrome'

	def test_page_url_title(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_page_url_title()

	def test_atm_services_context(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_atm_services_context()

	def test_online_services_context(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_online_services_context()

	def test_read_more_services_button(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_read_more_services_button()

	def test_read_more_news_button(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_read_more_news_button()

	def test_latest_news_title(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_latest_news_title()

	def test_parabank_admin_logo(self):

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_admin_logo()

	def test_parabank_logo(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_logo()

	def test_right_menu_home_button(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.right_menu_home_button_test()

	#@allure.story("Right Menu Buttons")
	@allure.title("Test \"About\" button")
	@allure.testcase('Test "About" button attributes')
	def test_right_menu_about_button(self):
		"""Context base elements validation > Home button:
		1. Open Home web page
		2. Do Home button verification: href + text
		"""
		# open web browser
		# with allure.step('1. Open test web page: {}.'.format(HomePageContext.URL)):
		self.open_web_browser(self.browser)
		# Context base elements validation:
		# with allure.step('2. Do Home button verification: href + text.'):
		self.right_menu_about_button_test()

	def test_right_menu_contact_button(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.right_menu_contact_button_test()

	def test_solutions_menu_items(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_solutions_menu_items()

	def test_customer_login(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_customer_login()

	def test_footer_items(self):

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_footer_items()


