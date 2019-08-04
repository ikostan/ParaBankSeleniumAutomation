import allure
from utils.screenshot import screenshot_on_fail
from tests.context_tests.services_page_context_case import ServicesPageContextTestCase


@allure.suite("Chrome Browser Context Testing")
@allure.sub_suite('Chrome Services Page Context Test')
@screenshot_on_fail()
class TestChromeServicesPageContext(ServicesPageContextTestCase):

	browser = 'chrome'

	def test_page_url(self):
		allure.dynamic.description("""
		Context base elements validation > Services page URL:
			1. Open Services page web page
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
		Context base elements validation > Services page title:
			1. Open Services page web page
			2. Do Services page title verification
		""")
		allure.dynamic.title("Services page title test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# open web browser
		self.open_web_browser(self.browser)

		# Verify web page title
		self.verify_page_title()

	def test_parabank_admin_logo(self):
		allure.dynamic.description("""
		Context base elements validation > Admin logo:
			1. Open Services page web page
			2. Do Admin logo verification
		""")
		allure.dynamic.title("Admin logo test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_admin_logo()

	def test_parabank_logo(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_logo()

	def test_right_menu(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_right_menu_buttons()

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


