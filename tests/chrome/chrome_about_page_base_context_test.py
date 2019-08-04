import allure
from utils.screenshot import screenshot_on_fail
from tests.context_tests.about_page_context_case import AboutPageContextTestCase


@allure.suite("Chrome Browser Context Testing")
@allure.sub_suite('Chrome About Page Context Test')
@screenshot_on_fail()
class TestChromeAboutPageContext(AboutPageContextTestCase):

	browser = 'chrome'

	def test_page_url_title(self):
		allure.dynamic.description("""
		Context base elements validation > About page URL:
			1. Open About page web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_page_url_title()

	def test_description_title_text(self):
		allure.dynamic.description("""
		Context base elements validation > About page title:
			1. Open About page web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page title test")

		# open web browser
		self.open_web_browser(self.browser)

		# verify description title text
		self.verify_description_title()

	def test_description_text(self):
		allure.dynamic.description("""
		Context base elements validation > About page description:
			1. Open About page web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page description test")

		# open web browser
		self.open_web_browser(self.browser)

		# verify description text
		self.verify_description_text()

	def test_parabank_admin_logo(self):
		allure.dynamic.description("""
		Context base elements validation > About page > ParaBank Admin logo:
			1. Open About page web page
			2. Do ParaBank Admin logo verification
		""")
		allure.dynamic.title("ParaBank Admin logo test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_admin_logo()

	def test_parabank_logo(self):
		allure.dynamic.description("""
		Context base elements validation > About page > ParaBank logo:
			1. Open About page web page
			2. Do ParaBank logo verification
		""")
		allure.dynamic.title("ParaBank logo test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_logo()

	def test_right_menu(self):
		allure.dynamic.description("""
		Context base elements validation > Right menu:
			1. Open About page web page
			2. Do Right menu logo verification
		""")
		allure.dynamic.title("Right menu test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_right_menu_buttons()

	def test_solutions_menu_items(self):
		allure.dynamic.description("""
		Context base elements validation > Solutions menu:
			1. Open About page web page
			2. Do Solutions menu logo verification
		""")
		allure.dynamic.title("Solutions menu test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_solutions_menu_items()

	def test_customer_login(self):
		allure.dynamic.description("""
		Context base elements validation > Customer Login:
			1. Open About page web page
			2. Do Customer Login verification
		""")
		allure.dynamic.title("Customer Login test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_customer_login()

	def test_footer_items(self):
		allure.dynamic.description("""
		Context base elements validation > Footer menu:
			1. Open About page web page
			2. Do Footer menu verification
		""")
		allure.dynamic.title("Footer menu test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_footer_items()


