import allure
from utils.screenshot import screenshot_on_fail
from tests.context_tests.home_page_context_case import TestHomePageContextCase


@allure.suite("Chrome Browser Context Testing")
@allure.sub_suite('Chrome Home Page Context Test')
@screenshot_on_fail()
class TestChromeHomePageContext(TestHomePageContextCase):

	browser = 'chrome'

	def test_page_url(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_page_url()
		allure.dynamic.title("Test web page URL")
		allure.dynamic.description("""
		Context base elements validation > Home page URL:
			1. Open Home web page
			2. Do URL verification
		""")

	def test_page_title(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_page_title()
		allure.dynamic.title("Test web page title")
		allure.dynamic.description("""
		Context base elements validation > Home page title:
			1. Open Home web page
			2. Do web page title verification
		""")

	def test_atm_services_context(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_atm_services_context()
		allure.dynamic.title("Test ATM services context")
		allure.dynamic.description("""
		Context elements validation > ATM services:
			1. Open Home web page
			2. Do ATM services context verification
		""")

	def test_online_services_context(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_online_services_context()
		allure.dynamic.title("Test Online services context")
		allure.dynamic.description("""
		Context elements validation > ATM services:
			1. Open Home web page
			2. Do Online services context verification
		""")

	def test_read_more_services_button(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_read_more_services_button()
		allure.dynamic.title("Test 'Read More' (services) button")
		allure.dynamic.description("""
		Context elements validation > 'Read More' (services) button:
			1. Open Home web page
			2. Do 'Read More' button verification: text + url
		""")

	def test_read_more_news_button(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_read_more_news_button()
		allure.dynamic.title("Test 'Read More' (news) button")
		allure.dynamic.description("""
		Context elements validation > 'Read More' (news) button:
			1. Open Home web page
			2. Do 'Read More' button verification: text + url
		""")

	def test_latest_news_title(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_latest_news_title()
		allure.dynamic.title("Test 'Latest News' title")
		allure.dynamic.description("""
		Context elements validation > 'Latest News' title:
			1. Open Home web page
			2. Do 'Latest News' title verification
		""")

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

	@allure.severity(allure.severity_level.CRITICAL)
	def test_right_menu_about_button(self):
		"""Context base elements validation > Home button:
		1. Open Home web page
		2. Do About button verification: href + text
		"""
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.right_menu_about_button_test()
		allure.dynamic.title("Test 'About' button")
		allure.dynamic.description("""
		Context base elements validation > Home button:
			1. Open Home web page
			2. Do 'About' button verification: href + text
		""")

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


