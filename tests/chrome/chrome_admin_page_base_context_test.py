import allure
from utils.screenshot import screenshot_on_fail
from tests.context_tests.admin_page_context_case import AdminPageContextTestCase


@allure.suite("Chrome Browser Context Testing")
@screenshot_on_fail()
class AdminPageContextTestCase(AdminPageContextTestCase):

	browser = 'chrome'

	def test_page_url_title(self):

		# open web browser
		self.open_web_browser(self.browser)
		self.verify_page_url_title()

	def test_parabank_admin_logo(self):

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


