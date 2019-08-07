import allure
from utils.screenshot import screenshot_on_fail
from tests.context_tests.register_context_case import RegisterContextCase


@allure.suite("Chrome Browser Context Testing")
@allure.sub_suite('Chrome Register Page Context Test')
@screenshot_on_fail()
class TestChromeRegisterPageContext(RegisterContextCase):
	
	browser = 'chrome'

	# Generic/Base context
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
		self.verify_parabank_admin_logo()

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
		self.verify_parabank_logo()

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
		self.verify_right_menu_home_button()

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
		self.verify_right_menu_contact_button()

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
		self.verify_right_menu_about_button()

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
		self.verify_solutions_menu_items()

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
		self.verify_customer_login()

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
		self.verify_footer_items()

	# Registration page context - Personal Info Context base elements validation
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
		self.verify_first_name_title()

	def test_last_name_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do Last Name title verification
		""")
		allure.dynamic.title("Last Name title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Personal Info Context base elements validation:
		self.verify_last_name_title()

	def test_address_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do Address title verification
		""")
		allure.dynamic.title("Address title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Personal Info Context base elements validation:
		self.verify_address_title()

	def test_city_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do City title verification
		""")
		allure.dynamic.title("City title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Personal Info Context base elements validation:
		self.verify_city_title()

	def test_state_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do State title verification
		""")
		allure.dynamic.title("State title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Personal Info Context base elements validation:
		self.verify_state_title()

	def test_zip_code_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do Zip Code title verification
		""")
		allure.dynamic.title("Zip Code title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Personal Info Context base elements validation:
		self.verify_zip_code_title()

	def test_phone_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do Phone title verification
		""")
		allure.dynamic.title("Phone title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Personal Info Context base elements validation:
		self.verify_phone_title()

	def test_ssn_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do SSN title verification
		""")
		allure.dynamic.title("SSN title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Personal Info Context base elements validation:
		self.verify_ssn_title()

	# Registration page context - Register web page context base elements validation
	def test_username_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do Username title verification
		""")
		allure.dynamic.title("Username title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Register web page elements validation:
		self.verify_username_title()

	def test_password_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do Password title verification
		""")
		allure.dynamic.title("Password title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Register web page elements validation:
		self.verify_password_title()

	def test_confirm_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do Confirm title verification
		""")
		allure.dynamic.title("Confirm title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Register web page elements validation:
		self.verify_confirm_title()

	def test_register_button(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do "Register" button verification
		""")
		allure.dynamic.title("\"Register\" button test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# open web browser
		self.open_web_browser(self.browser)

		# Register web page elements validation:
		self.verify_register_button()
