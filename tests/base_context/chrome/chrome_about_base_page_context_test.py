import allure
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from page_models.about_page_model import AboutPageModel
from tests.context_tests.about_page_context_case import AboutPageContextCase
from expected_results.page_context.about_page_context import AboutPageContext


@allure.suite("Base Context Testing")
@allure.sub_suite('Chrome Browser')
@allure.feature("About Base Page")
@screenshot_on_fail()
class TestChromeAboutBasePageContext(AboutPageContextCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = 'chrome'
			cls.page_model = AboutPageModel
			cls.page_context = AboutPageContext
			cls.page = open_web_browser(browser=cls.browser,
			                            page_model=cls.page_model,
			                            page_context=cls.page_context)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def test_page_url(self):
		allure.dynamic.description("""
		Context base elements validation > About page URL:
			1. Open About web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")

		# Verify Web Page URL
		self.verify_page_url()

	def test_page_title(self):
		allure.dynamic.description("""
		Context base elements validation > About page URL:
			1. Open About web page
			2. Do Title verification
		""")
		allure.dynamic.title("Web page title test")

		# Verify Web Page Title
		self.verify_page_title()

	@allure.feature("Base Page")
	def test_parabank_admin_logo(self):
		allure.dynamic.description("""
		Context base elements validation > About page > ParaBank Admin logo:
			1. Open About web page
			2. Do ParaBank Admin logo verification
		""")
		allure.dynamic.title("ParaBank Admin logo test")

		# Context base elements validation:
		self.verify_parabank_admin_logo()

	@allure.feature("Base Page")
	def test_parabank_logo(self):
		allure.dynamic.description("""
		Context base elements validation > About page > ParaBank logo:
			1. Open About web page
			2. Do ParaBank logo verification
		""")
		allure.dynamic.title("ParaBank logo test")

		# Context base elements validation:
		self.verify_parabank_logo()

	@allure.feature("Base Page")
	def test_right_menu_home_button(self):
		allure.dynamic.description("""
		Context base elements validation > Right menu:
			1. Open About web page
			2. Do Right menu home button verification
		""")
		allure.dynamic.title("Right menu test")

		# Context base elements validation:
		self.verify_right_menu_home_button()

	@allure.feature("Base Page")
	def test_right_menu_contact_button(self):
		allure.dynamic.description("""
		Context base elements validation > Right menu:
			1. Open About web page
			2. Do Right menu contact button verification
		""")
		allure.dynamic.title("Right menu test")

		# Context base elements validation:
		self.verify_right_menu_contact_button()

	@allure.feature("Base Page")
	def test_right_menu_about_button(self):
		allure.dynamic.description("""
		Context base elements validation > Right menu:
			1. Open About web page
			2. Do Right menu about button verification
		""")
		allure.dynamic.title("Right menu test")

		# Context base elements validation:
		self.verify_right_menu_about_button()

	@allure.feature("Base Page")
	def test_solutions_menu_items(self):
		allure.dynamic.description("""
		Context base elements validation > Solutions menu:
			1. Open About web page
			2. Do Solutions menu logo verification
		""")
		allure.dynamic.title("Solutions menu test")

		# Context base elements validation:
		self.verify_solutions_menu_items()

	@allure.feature("Base Page")
	def test_customer_login(self):
		allure.dynamic.description("""
		Context base elements validation > Customer Login:
			1. Open About web page
			2. Do Customer Login verification
		""")
		allure.dynamic.title("Customer Login test")

		# Context base elements validation:
		self.verify_customer_login()

	@allure.feature("Base Page")
	def test_footer_items(self):
		allure.dynamic.description("""
		Context base elements validation > Footer menu:
			1. Open About web page
			2. Do Footer menu verification
		""")
		allure.dynamic.title("Footer menu test")

		# Context base elements validation:
		self.verify_footer_items()

