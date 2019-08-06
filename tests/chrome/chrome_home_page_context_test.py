import allure
from utils.screenshot import screenshot_on_fail
from tests.context_tests.home_page_context_case import TestHomePageContextCase


@allure.suite("Chrome Browser Context Testing")
@allure.sub_suite('Chrome Home Page Context Test')
@screenshot_on_fail()
class TestChromeHomePageContext(TestHomePageContextCase):

	browser = 'chrome'

	@allure.feature("Base Page")
	def test_page_url(self):

		allure.dynamic.description("""
		Context base elements validation > Home page URL:
			1. Open Home web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")

		# open web browser
		self.open_web_browser(self.browser)

		# test url
		self.verify_page_url()

	@allure.feature("Base Page")
	def test_page_title(self):
		allure.dynamic.description("""
		Context base elements validation > Home page title:
			1. Open Home web page
			2. Do web page title verification
		""")
		allure.dynamic.title("Web page title test")

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_page_title()

	@allure.feature("Home Page")
	def test_atm_services_context(self):
		allure.dynamic.description("""
		Home page Context elements validation > ATM services:
			1. Open Home web page
			2. Do ATM services context verification
		""")
		allure.dynamic.title("ATM services context test")

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_atm_services_context()

	@allure.feature("Home Page")
	def test_online_services_context(self):
		allure.dynamic.description("""
		Home page Context elements validation > ATM services:
			1. Open Home web page
			2. Do Online services context verification
		""")
		allure.dynamic.title("Online services context test")

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_online_services_context()

	@allure.feature("Home Page")
	def test_read_more_services_button(self):
		allure.dynamic.description("""
		Home page Context elements validation > 'Read More' (services) button:
			1. Open Home web page
			2. Do 'Read More' button verification
		""")
		allure.dynamic.title("'Read More' (services) button test")

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_read_more_services_button()

	@allure.feature("Home Page")
	def test_read_more_news_button(self):
		allure.dynamic.description("""
		Home page Context elements validation > 'Read More' (news) button:
			1. Open Home web page
			2. Do 'Read More' button verification
		""")
		allure.dynamic.title("'Read More' (news) button test")

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_read_more_news_button()

	@allure.feature("Home Page")
	def test_latest_news_title(self):
		allure.dynamic.description("""
		Home page Context elements validation > 'Latest News' title:
			1. Open Home web page
			2. Do 'Latest News' title verification
		""")
		allure.dynamic.title("'Latest News' title test")

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_latest_news_title()

	@allure.feature("Base Page")
	def test_parabank_admin_logo(self):
		allure.dynamic.description("""
		Context base elements validation > Admin logo:
			1. Open Home web page
			2. Do Admin logo verification
		""")
		allure.dynamic.title("Admin logo test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_admin_logo()

	@allure.feature("Base Page")
	def test_parabank_logo(self):
		allure.dynamic.description("""
		Context base elements validation > 'ParaBank' logo:
			1. Open Home web page
			2. Do Admin logo verification
		""")
		allure.dynamic.title("'ParaBank' logo test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_logo()

	@allure.feature("Base Page")
	def test_right_menu_home_button(self):
		allure.dynamic.description("""
		Context base elements validation > 'Home' button:
			1. Open Home web page
			2. Do 'Home' button (right menu) verification
		""")
		allure.dynamic.title("'Home' button (right menu) test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.right_menu_home_button_test()

	@allure.feature("Base Page")
	def test_right_menu_about_button(self):
		"""Context base elements validation > Home button:
		1. Open Home web page
		2. Do About button verification: href + text
		"""
		allure.dynamic.description("""
		Context base elements validation > 'About' button:
			1. Open Home web page
			2. Do 'About' button (right menu) verification
		""")
		allure.dynamic.title("'About' button (right menu) test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.right_menu_about_button_test()

	@allure.feature("Base Page")
	def test_right_menu_contact_button(self):
		allure.dynamic.description("""
		Context base elements validation > 'Contact' button:
			1. Open Home web page
			2. Do 'Contact' button (right menu) verification
		""")
		allure.dynamic.title("'Contact' button (right menu) test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.right_menu_contact_button_test()

	@allure.feature("Base Page")
	def test_solutions_menu_items(self):
		allure.dynamic.description("""
		Context base elements validation > 'Solutions' menu items:
			1. Open Home web page
			2. Do 'Solutions' menu items verification
		""")
		allure.dynamic.title("'Solutions' menu items test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_solutions_menu_items()

	@allure.feature("Base Page")
	def test_customer_login(self):
		allure.dynamic.description("""
		Context base elements validation > 'Customer Login':
			1. Open Home web page
			2. Do 'Customer Login' items verification
		""")
		allure.dynamic.title("'Customer Login' test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_customer_login()

	@allure.feature("Base Page")
	def test_footer_items(self):
		allure.dynamic.description("""
		Context base elements validation > 'Footer':
			1. Open Home web page
			2. Do 'Footer' items verification
		""")

		allure.dynamic.title("'Footer' test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_footer_items()



