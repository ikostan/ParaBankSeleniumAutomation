import allure
from utils.driver import Driver
from utils.screenshot import screenshot_on_fail
from page_models.admin_page_model import AdminPageModel
from tests.context_tests.base_context_case import TestBaseContextCase
from expected_results.page_context.admin_page_context import AdminPageContext


@allure.feature("Admin Page")
@allure.story('Admin Context')
@screenshot_on_fail()
class AdminPageContextTestCase(TestBaseContextCase):

	def open_web_browser(self, browser):

		# Open web page
		with allure.step("Open web browser on: {}".format(AdminPageContext.URL)):
			driver = Driver(browser)
			self.page = AdminPageModel(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
			self.page.go()

	def verify_page_url(self):

		with allure.step("Admin page URL test"):
			self.assertEqual(AdminPageContext.URL,
			                 self.page.url)

	def verify_page_title(self):

		with allure.step("Admin page title test"):
			self.assertEqual(AdminPageContext.TITLE,
			                 self.page.title)

	def verify_parabank_admin_logo(self):

		# Context base elements validation:
		self.parabank_admin_logo_test()

	def verify_parabank_logo(self):

		# Context base elements validation:
		self.parabank_logo_test()

	def verify_right_menu_buttons(self):

		# Context base elements validation:
		self.right_menu_buttons_test()

	def verify_solutions_menu_items(self):

		# Context base elements validation:
		self.solutions_menu_items_test()

	def verify_customer_login(self):

		# Context base elements validation:
		self.customer_login_test()

	def verify_footer_items(self):

		# Context base elements validation:
		self.footer_items_test()


