import allure
from utils.screenshot import screenshot_on_fail
from tests.context_tests.register_context_case import RegisterContextCase


@allure.suite("Chrome Browser Context Testing")
@allure.sub_suite('Chrome Register Page Context Test')
@screenshot_on_fail()
class TestChromeRegisterPageContext(RegisterContextCase):
	
	browser = 'chrome'

	def test_page_url(self):
		allure.dynamic.description("""
		ontext base elements validation > Register page URL:
			1. Open Register page web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Verify web page url
		self.verify_page_url()

	def test_page_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register page title:
			1. Open Register page web page
			2. Do Register page title verification
		""")
		allure.dynamic.title("Register page title test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# open web browser
		self.open_web_browser(self.browser)

		# Verify web page title
		self.verify_page_title()

	def test_parabank_admin_logo(self):
		allure.dynamic.description("""
		Context base elements validation > Admin logo:
			1. Open Register page web page
			2. Do Admin logo verification
		""")
		allure.dynamic.title("Admin logo test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.parabank_admin_logo_test()

	def test_parabank_logo(self):
		allure.dynamic.description("""
		Context base elements validation > ParaBank logo:
			1. Open Register web page
			2. Do ParaBank logo verification
		""")
		allure.dynamic.title("ParaBank logo test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.parabank_logo_test()

	def test_right_menu_home_button(self):
		allure.dynamic.description("""
		Context base elements validation > Right menu:
			1. Open Register web page
			2. Do Right menu Home button verification
		""")
		allure.dynamic.title("Right menu Home button test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.right_menu_home_button_test()

	def test_right_menu_contact_button(self):
		allure.dynamic.description("""
		Context base elements validation > Right menu:
			1. Open Register web page
			2. Do Right menu Contact button verification
		""")
		allure.dynamic.title("Right menu Contact button test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.right_menu_contact_button_test()

	def test_right_menu_about_button(self):
		allure.dynamic.description("""
		Context base elements validation > Right menu:
			1. Open Register web page
			2. Do Right menu About button verification
		""")
		allure.dynamic.title("Right menu About button test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.right_menu_about_button_test()

	def test_solutions_menu_items(self):
		allure.dynamic.description("""
		Context base elements validation > Solution menu:
			1. Open Register web page
			2. Do Solution verification
		""")
		allure.dynamic.title("Solution menu test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.solutions_menu_items_test()

	def test_customer_login(self):
		allure.dynamic.description("""
		Context base elements validation > Customer Login:
			1. Open Register web page
			2. Do Customer Login verification
		""")
		allure.dynamic.title("Customer Login test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.customer_login_test()

	def test_footer_items(self):
		allure.dynamic.description("""
		Context base elements validation > Footer:
			1. Open Register web page
			2. Do Footer verification
		""")
		allure.dynamic.title("Footer test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.footer_items_test()

	def test_first_name_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do First Name title verification
		""")
		allure.dynamic.title("First Name title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Personal Info Context base elements validation:
		self.first_name_title_test()
