import allure
from allure import severity_level
from utils.screenshot import screenshot_on_fail
from tests.context_tests.home_page_context_case import HomePageContextTestCase


@screenshot_on_fail()
class HomePageContextTestCase(HomePageContextTestCase):

	browser = 'chrome'

	@allure.feature("Home Page Context.")
	@allure.story("ParaBank URL and Web Page Title verification")
	@allure.severity(severity_level.MINOR)
	def test_page_url_title(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_page_url_title()

	@allure.feature("Home Page Context.")
	@allure.story("ATM Services items verification")
	@allure.severity(severity_level.MINOR)
	def test_atm_services_context(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_atm_services_context()

	@allure.feature("Home Page Context.")
	@allure.story("Online Services items verification")
	@allure.severity(severity_level.MINOR)
	def test_online_services_context(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_online_services_context()

	@allure.feature("Home Page Context.")
	@allure.story("Services > Read More button verification")
	@allure.severity(severity_level.MINOR)
	def test_read_more_services_button(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_read_more_services_button()

	@allure.feature("Home Page Context.")
	@allure.story("News Services > Read More button verification")
	@allure.severity(severity_level.MINOR)
	def test_read_more_news_button(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_read_more_news_button()

	@allure.feature("Home Page Context.")
	@allure.story("Latest News title verification")
	@allure.severity(severity_level.MINOR)
	def test_latest_news_title(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_latest_news_title()

	@allure.feature("Home Page Context.")
	@allure.story("Admin Logo verification")
	@allure.severity(severity_level.MINOR)
	def test_parabank_admin_logo(self):

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_admin_logo()

	@allure.feature("Home Page Context.")
	@allure.story("ParaBank Logo verification")
	@allure.severity(severity_level.MINOR)
	def test_parabank_logo(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_logo()

	@allure.feature("Home Page Context.")
	@allure.story("Welcome to ParaBank (Right Menu) items verification")
	@allure.severity(severity_level.MINOR)
	def test_right_menu(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_right_menu_buttons()

	@allure.feature("Home Page Context.")
	@allure.story("Solutions menu items verification")
	@allure.severity(severity_level.NORMAL)
	def test_solutions_menu_items(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_solutions_menu_items()

	@allure.feature("Home Page Context.")
	@allure.story("Customer Login verification")
	@allure.severity(severity_level.BLOCKER)
	def test_customer_login(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_customer_login()

	@allure.feature("Home Page Context.")
	@allure.story("Footer menu items verification")
	@allure.severity(severity_level.NORMAL)
	def test_footer_items(self):

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_footer_items()


