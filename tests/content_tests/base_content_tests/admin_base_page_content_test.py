#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.browser_configuration import browser_configuration

from page_object_models.admin_page_model import AdminPageModel
from expected_results.page_content.admin_page_content import AdminPageContent
from tests.content_tests.base_cases.base_content_case import BaseContentCase


@allure.epic('Page Content')
@allure.parent_suite('Page Base Content')
@allure.suite('Admin Page Content')
@allure.sub_suite("Admin Page Base Content")
@allure.feature("Base Page")
@allure.story('Admin Content')
@screenshot_on_fail()
class TestAdminBasePageContent(BaseContentCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = browser_configuration()
			cls.page_model = AdminPageModel
			cls.page_content = AdminPageContent
			cls.page = open_web_browser(browser=cls.browser,
			                            page_model=cls.page_model,
			                            page_content=cls.page_content)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	'''
	def test_page_url(self):

		allure.dynamic.description("""
		Content base elements validation > Admin page URL:
			1. Open Admin web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# test url
		self.verify_page_url()

	def test_page_title(self):
		allure.dynamic.description("""
		Content base elements validation > Admin page title:
			1. Open Admin web page
			2. Do web page title verification
		""")
		allure.dynamic.title("Web page title test")

		# Verify Page Title
		self.verify_page_title()
	'''

	# Base Page Content
	@allure.feature("Base Page")
	def test_parabank_admin_logo(self):
		allure.dynamic.description("""
		Content base elements validation > Admin logo:
			1. Open Admin web page
			2. Do Admin logo verification
		""")
		allure.dynamic.title("Admin logo test")

		# Content base elements validation:
		self.verify_parabank_admin_logo()

	@allure.feature("Base Page")
	def test_parabank_logo(self):
		allure.dynamic.description("""
		Content base elements validation > 'ParaBank' logo:
			1. Open Admin web page
			2. Do Admin logo verification
		""")
		allure.dynamic.title("'ParaBank' logo test")

		# Content base elements validation:
		self.verify_parabank_logo()

	@allure.feature("Base Page")
	def test_right_menu_home_button(self):
		allure.dynamic.description("""
		Content base elements validation > 'Home' button:
			1. Open Admin web page
			2. Do 'Home' button (right menu) verification
		""")
		allure.dynamic.title("Right menu > 'Home' button test")

		# Content base elements validation:
		self.verify_right_menu_home_button()

	@allure.feature("Base Page")
	def test_right_menu_about_button(self):
		"""Content base elements validation > About button:
		1. Open Home web page
		2. Do About button verification: href + text
		"""
		allure.dynamic.description("""
		Content base elements validation > 'About' button:
			1. Open Admin web page
			2. Do 'About' button (right menu) verification
		""")
		allure.dynamic.title("Right menu > 'About' button test")

		# Content base elements validation:
		self.verify_right_menu_about_button()

	@allure.feature("Base Page")
	def test_right_menu_contact_button(self):
		allure.dynamic.description("""
		Content base elements validation > 'Contact' button:
			1. Open Admin web page
			2. Do 'Contact' button (right menu) verification
		""")
		allure.dynamic.title("Right menu > 'Contact' button test")

		# Content base elements validation:
		self.verify_right_menu_contact_button()

	@allure.feature("Base Page")
	def test_solutions_menu_items(self):
		allure.dynamic.description("""
		Content base elements validation > 'Solutions' menu items:
			1. Open Admin web page
			2. Do 'Solutions' menu items verification
		""")
		allure.dynamic.title("'Solutions' menu items test")

		# Content base elements validation:
		self.verify_solutions_menu_items()

	@allure.feature("Base Page")
	def test_customer_login(self):
		allure.dynamic.description("""
		Content base elements validation > 'Customer Login':
			1. Open Admin web page
			2. Do 'Customer Login' items verification
		""")
		allure.dynamic.title("'Customer Login' test")

		# Content base elements validation:
		self.verify_customer_login()

	@allure.feature("Base Page")
	def test_footer_home_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open Admin web page
			2. Do 'Footer' > 'Home' item verification
		""")

		allure.dynamic.title("'Footer' > 'Home' item test")
		self.verify_footer_home_item()

	@allure.feature("Base Page")
	def test_footer_about_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open Admin web page
			2. Do 'Footer' > 'About Us' item verification
		""")

		allure.dynamic.title("'Footer' > 'About Us' item test")
		self.verify_footer_about_item()

	@allure.feature("Base Page")
	def test_footer_services_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open Admin web page
			2. Do 'Footer' > 'Services' item verification
		""")

		allure.dynamic.title("'Footer' > 'Services' test")
		self.verify_footer_services_item()

	@allure.feature("Base Page")
	def test_footer_products_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open Admin web page
			2. Do 'Footer' > 'Products' item verification
		""")

		allure.dynamic.title("'Footer' > 'Products' item test")
		self.verify_footer_products_item()

	@allure.feature("Base Page")
	def test_footer_locations_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open Admin web page
			2. Do 'Footer' > 'Locations' item verification
		""")

		allure.dynamic.title("'Footer' > 'Locations' item test")
		self.verify_footer_locations_item()

	@allure.feature("Base Page")
	def test_footer_forum_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open Admin web page
			2. Do 'Footer' > 'Forum' item verification
		""")

		allure.dynamic.title("'Footer' > 'Forum' test")
		self.verify_footer_forum_item()

	@allure.feature("Base Page")
	def test_footer_site_map_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open Admin web page
			2. Do 'Footer' > 'Site Map' item verification
		""")

		allure.dynamic.title("'Footer' > 'Site Map' item test")
		self.verify_footer_site_map_item()

	@allure.feature("Base Page")
	def test_footer_contact_us_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open Admin web page
			2. Do 'Footer' > 'Contact Us' item verification
		""")

		allure.dynamic.title("'Footer' > 'Contact Us' item test")
		self.verify_footer_contact_us_item()

	@allure.feature("Base Page")
	def test_footer_copyright_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open Admin web page
			2. Do 'Footer' > copyright item verification
		""")

		allure.dynamic.title("'Footer' > copyright item test")
		self.verify_footer_copyright_item()

	@allure.feature("Base Page")
	def test_footer_visit_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open Admin web page
			2. Do 'Footer' > 'Visit' item verification
		""")

		allure.dynamic.title("'Footer' > Visit us item test")
		self.verify_footer_visit_item()
