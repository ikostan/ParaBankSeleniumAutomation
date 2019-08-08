import allure
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from page_models.services_page_model import ServicesPageModel
from tests.context_tests.services_page_context_case import ServicesPageContextCase
from expected_results.page_context.services_page_context import ServicesPageContext


@allure.suite("Chrome Browser Context Testing")
@allure.sub_suite('Chrome Services Page Context Test')
@screenshot_on_fail()
class TestChromeServicesPageContext(ServicesPageContextCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = 'chrome'
			cls.page_model = ServicesPageModel
			cls.page_context = ServicesPageContext
			cls.page = open_web_browser(browser=cls.browser,
			                            page_model=cls.page_model,
			                            page_context=cls.page_context)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	@allure.feature("Services Page")
	def test_page_url(self):
		allure.dynamic.description("""
		Context base elements validation > Services page URL:
			1. Open Services web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# open web browser
		# self.open_web_browser(self.browser)

		# Verify web page url
		self.verify_page_url()

	@allure.feature("Services Page")
	def test_page_title(self):
		allure.dynamic.description("""
		Context base elements validation > Services page title:
			1. Open Services web page
			2. Do Services page title verification
		""")
		allure.dynamic.title("Services page title test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# open web browser
		# self.open_web_browser(self.browser)

		# Verify web page title
		self.verify_page_title()

	# Services Context Testing

	'''
	# Base Context test
	@allure.feature("Base Page")
	def test_parabank_admin_logo(self):
		allure.dynamic.description("""
		Context base elements validation > Admin logo:
			1. Open Services web page
			2. Do Admin logo verification
		""")
		allure.dynamic.title("Admin logo test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# open web browser
		# self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_admin_logo()

	@allure.feature("Base Page")
	def test_parabank_logo(self):
		allure.dynamic.description("""
		Context base elements validation > ParaBank logo:
			1. Open Services page web page
			2. Do ParaBank logo verification
		""")
		allure.dynamic.title("ParaBank logo test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		# self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_logo()

	@allure.feature("Base Page")
	def test_right_menu_home_button(self):
		allure.dynamic.description("""
		Context base elements validation > Right menu:
			1. Open Services web page
			2. Do Right menu Home button verification
		""")
		allure.dynamic.title("Right menu Home button test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# open web browser
		# self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_right_menu_home_button()

	@allure.feature("Base Page")
	def test_right_menu_contact_button(self):
		allure.dynamic.description("""
		Context base elements validation > Right menu:
			1. Open Services web page
			2. Do Right menu Contact button verification
		""")
		allure.dynamic.title("Right menu Contact button test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# open web browser
		# self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_right_menu_contact_button()

	@allure.feature("Base Page")
	def test_right_menu_about_button(self):
		allure.dynamic.description("""
		Context base elements validation > Right menu:
			1. Open Services web page
			2. Do Right menu About button verification
		""")
		allure.dynamic.title("Right menu About button test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# open web browser
		# self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_right_menu_about_button()

	@allure.feature("Base Page")
	def test_solutions_menu_items(self):
		allure.dynamic.description("""
		Context base elements validation > Solution menu:
			1. Open Services web page
			2. Do Solution verification
		""")
		allure.dynamic.title("Solution menu test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# open web browser
		# self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_solutions_menu_items()

	@allure.feature("Base Page")
	def test_customer_login(self):
		allure.dynamic.description("""
		Context base elements validation > Customer Login:
			1. Open Services web page
			2. Do Customer Login verification
		""")
		allure.dynamic.title("Customer Login test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# open web browser
		# self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_customer_login()

	# TODO: remove this one
	@allure.feature("Base Page")
	def test_footer_items(self):
		allure.dynamic.description("""
		Context base elements validation > Footer:
			1. Open Services web page
			2. Do Footer verification
		""")
		allure.dynamic.title("Footer test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# open web browser
		# self.open_web_browser(self.browser)

		# Context base elements validation:
		# self.verify_footer_items()
		pass

	'''
