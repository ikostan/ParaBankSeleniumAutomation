import allure
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.http_status_code import get_http_status_code
from page_models.services_page_model import ServicesPageModel
from tests.context_tests.services_page_context_case import ServicesPageContextCase
from expected_results.page_context.services_page_context import ServicesPageContext


@allure.suite("Chrome Browser Context Testing")
@allure.sub_suite('Chrome Services Page Context Test')
@allure.feature("Services Page")
@screenshot_on_fail()
class TestChromeServicesPageContext(ServicesPageContextCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = 'chrome'
			cls.page_model = ServicesPageModel
			cls.page_context = ServicesPageContext
			get_http_status_code(ServicesPageContext.URL)
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

		# Verify web page title
		self.verify_page_title()

	# Services Context Testing

