import allure
from utils.screenshot import screenshot_on_fail
from tests.context_tests.admin_page_context_case import AdminPageContextCase


@allure.suite("Chrome Browser Context Testing")
@allure.sub_suite('Chrome Admin Page Context Test')
@screenshot_on_fail()
class TestChromeAdminPageContext(AdminPageContextCase):

	browser = 'chrome'

	def test_page_url(self):
		allure.dynamic.description("""
		Context base elements validation > Admin page URL:
			1. Open Admin web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")

		# open web browser
		self.open_web_browser(self.browser)

		# verify web page url
		self.verify_page_url()

	def test_page_title(self):
		allure.dynamic.description("""
		Context base elements validation > Admin page URL:
			1. Open Admin web page
			2. Do Title verification
		""")
		allure.dynamic.title("Web page Title test")

		# open web browser
		self.open_web_browser(self.browser)

		# verify web page url
		self.verify_page_title()

	def test_parabank_admin_logo(self):
		allure.dynamic.description("""
		Context base elements validation > 'Admin' logo:
			1. Open Admin web page
			2. Do 'Admin' logo verification
		""")
		allure.dynamic.title("Admin logo test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_admin_logo()

	def test_parabank_logo(self):
		allure.dynamic.description("""
		Context base elements validation > 'ParaBank' logo:
			1. Open Admin web page
			2. Do 'ParaBank' logo verification
		""")
		allure.dynamic.title("ParaBank logo test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_parabank_logo()

	def test_right_menu_home_button(self):
		allure.dynamic.description("""
		Context base elements validation > right menu:
			1. Open Admin web page
			2. Do right Right menu Home button verification
		""")
		allure.dynamic.title("Right menu Home button test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_right_menu_home_button()

	def test_right_menu_contact_button(self):
		allure.dynamic.description("""
		Context base elements validation > right menu:
			1. Open Admin web page
			2. Do Right menu Contact button verification
		""")
		allure.dynamic.title("Right menu Contact button test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_right_menu_contact_button()

	def test_right_menu_about_button(self):
		allure.dynamic.description("""
		Context base elements validation > right menu:
			1. Open Admin web page
			2. Do Right menu About button verification
		""")
		allure.dynamic.title("Right menu About button test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_right_menu_about_button()

	def test_solutions_menu_items(self):
		allure.dynamic.description("""
		Context base elements validation > 'Solutions' menu:
			1. Open Admin web page
			2. Do 'Solutions' menu items verification
		""")
		allure.dynamic.title("Solutions menu items test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_solutions_menu_items()

	def test_customer_login(self):
		allure.dynamic.description("""
		Context base elements validation > Customer Login:
			1. Open Admin web page
			2. Do 'Customer Login' items verification
		""")
		allure.dynamic.title("Customer Login items test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_customer_login()

	def test_footer_items(self):
		allure.dynamic.description("""
		Context base elements validation > Footer:
			1. Open Admin web page
			2. Do 'Footer' items verification
		""")
		allure.dynamic.title("Footer items test")

		# open web browser
		self.open_web_browser(self.browser)

		# Context base elements validation:
		self.verify_footer_items()


