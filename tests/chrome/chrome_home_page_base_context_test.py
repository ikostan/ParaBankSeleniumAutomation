import allure
from allure import severity_level
from utils.screenshot import screenshot_on_fail
from tests.context_tests.home_page_context_case import HomePageContextTestCase


@screenshot_on_fail()
class ChromeHomePageContextTestCase(HomePageContextTestCase):

	browser = 'chrome'

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("ParaBank URL and Web Page Title verification")
	@allure.severity(severity_level.MINOR)
	def test_page_url_title(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_page_url_title()

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("ATM Services items verification")
	@allure.severity(severity_level.MINOR)
	def test_atm_services_context(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_atm_services_context()

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("Online Services items verification")
	@allure.severity(severity_level.MINOR)
	def test_online_services_context(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_online_services_context()

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("Services > Read More button verification")
	@allure.severity(severity_level.MINOR)
	def test_read_more_services_button(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_read_more_services_button()

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("News Services > Read More button verification")
	@allure.severity(severity_level.MINOR)
	def test_read_more_news_button(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_read_more_news_button()

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("Latest News title verification")
	@allure.severity(severity_level.MINOR)
	def test_latest_news_title(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_latest_news_title()

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("Admin Logo verification")
	@allure.severity(severity_level.MINOR)
	def test_parabank_admin_logo(self):

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_admin_logo()

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("ParaBank Logo verification")
	@allure.severity(severity_level.MINOR)
	def test_parabank_logo(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_logo()

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("Welcome to ParaBank (Right Menu) > Home button verification")
	@allure.severity(severity_level.MINOR)
	def test_right_menu_home_button(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.right_menu_home_button_test()

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("Welcome to ParaBank (Right Menu) > About button verification")
	@allure.severity(severity_level.MINOR)
	@allure.step("Verify Home button properties")
	@allure.description("Home web page > Home button verification: href + text")
	def test_right_menu_about_button(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.right_menu_about_button_test()

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("Welcome to ParaBank (Right Menu) > Contact button verification")
	@allure.severity(severity_level.MINOR)
	def test_right_menu_contact_button(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.right_menu_contact_button_test()

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("Solutions menu items verification")
	@allure.severity(severity_level.NORMAL)
	def test_solutions_menu_items(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_solutions_menu_items()

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("Customer Login verification")
	@allure.severity(severity_level.BLOCKER)
	def test_customer_login(self):
		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_customer_login()

	@allure.epic("ParaBank Web App")
	@allure.feature("Home Page Context.")
	@allure.story("Footer menu items verification")
	@allure.severity(severity_level.NORMAL)
	def test_footer_items(self):

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_footer_items()


