#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from tests.config import Config
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser

from page_object_models.about_page_model import AboutPageModel
from expected_results.page_content.about_page_content import AboutPageContent
from tests.content_tests.base_cases.base_content_case import BaseContentCase


@allure.epic('Page Content')
@allure.parent_suite('Page Base Content')
@allure.suite('About Page Content')
@allure.sub_suite("About Page Base Content")
@allure.feature("Base Page")
@allure.story('About Content')
@screenshot_on_fail()
class TestAboutBasePageContent(BaseContentCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.page_model = AboutPageModel
			cls.page_content = AboutPageContent
			cls.config = Config()
			cls.page = open_web_browser(config=cls.config,
			                            page_model=cls.page_model,
			                            page_content=cls.page_content)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	# Base Page Content
	def test_parabank_admin_logo(self):
		allure.dynamic.description("""
		Content base elements validation > Admin logo:
			1. Open About web page
			2. Do Admin logo verification
		""")
		allure.dynamic.title("Admin logo test")

		# Content base elements validation:
		self.verify_parabank_admin_logo()

	def test_parabank_logo(self):
		allure.dynamic.description("""
		Content base elements validation > 'ParaBank' logo:
			1. Open About web page
			2. Do Admin logo verification
		""")
		allure.dynamic.title("'ParaBank' logo test")

		# Content base elements validation:
		self.verify_parabank_logo()

	def test_right_menu_home_button(self):
		allure.dynamic.description("""
		Content base elements validation > 'Home' button:
			1. Open About web page
			2. Do 'Home' button (right menu) verification
		""")
		allure.dynamic.title("Right menu > 'Home' button test")

		# Content base elements validation:
		self.verify_right_menu_home_button()

	def test_right_menu_about_button(self):
		"""Content base elements validation > About button:
		1. Open About web page
		2. Do About button verification: href + text
		"""
		allure.dynamic.description("""
		Content base elements validation > 'About' button:
			1. Open About web page
			2. Do 'About' button (right menu) verification
		""")
		allure.dynamic.title("Right menu > 'About' button test")

		# Content base elements validation:
		self.verify_right_menu_about_button()

	def test_right_menu_contact_button(self):
		allure.dynamic.description("""
		Content base elements validation > 'Contact' button:
			1. Open About web page
			2. Do 'Contact' button (right menu) verification
		""")
		allure.dynamic.title("Right menu > 'Contact' button test")

		# Content base elements validation:
		self.verify_right_menu_contact_button()

	def test_solutions_menu_items(self):
		allure.dynamic.description("""
		Content base elements validation > 'Solutions' menu items:
			1. Open About web page
			2. Do 'Solutions' menu items verification
		""")
		allure.dynamic.title("'Solutions' menu items test")

		# Content base elements validation:
		self.verify_solutions_menu_items()

	def test_customer_login(self):
		allure.dynamic.description("""
		Content base elements validation > 'Customer Login':
			1. Open About web page
			2. Do 'Customer Login' items verification
		""")
		allure.dynamic.title("'Customer Login' test")

		# Content base elements validation:
		self.verify_customer_login()

	def test_footer_home_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open About web page
			2. Do 'Footer' > 'Home' item verification
		""")

		allure.dynamic.title("'Footer' > 'Home' item test")
		self.verify_footer_home_item()

	def test_footer_about_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open About web page
			2. Do 'Footer' > 'About Us' item verification
		""")

		allure.dynamic.title("'Footer' > 'About Us' item test")
		self.verify_footer_about_item()

	def test_footer_services_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open About web page
			2. Do 'Footer' > 'Services' item verification
		""")

		allure.dynamic.title("'Footer' > 'Services' test")
		self.verify_footer_services_item()

	def test_footer_products_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open About web page
			2. Do 'Footer' > 'Products' item verification
		""")

		allure.dynamic.title("'Footer' > 'Products' item test")
		self.verify_footer_products_item()

	def test_footer_locations_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open About web page
			2. Do 'Footer' > 'Locations' item verification
		""")

		allure.dynamic.title("'Footer' > 'Locations' item test")
		self.verify_footer_locations_item()

	def test_footer_forum_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open About web page
			2. Do 'Footer' > 'Forum' item verification
		""")

		allure.dynamic.title("'Footer' > 'Forum' test")
		self.verify_footer_forum_item()

	def test_footer_site_map_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open About web page
			2. Do 'Footer' > 'Site Map' item verification
		""")

		allure.dynamic.title("'Footer' > 'Site Map' item test")
		self.verify_footer_site_map_item()

	def test_footer_contact_us_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open About web page
			2. Do 'Footer' > 'Contact Us' item verification
		""")

		allure.dynamic.title("'Footer' > 'Contact Us' item test")
		self.verify_footer_contact_us_item()

	def test_footer_copyright_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open About web page
			2. Do 'Footer' > copyright item verification
		""")

		allure.dynamic.title("'Footer' > copyright item test")
		self.verify_footer_copyright_item()

	def test_footer_visit_item(self):
		allure.dynamic.description("""
		Content base elements validation > 'Footer':
			1. Open About web page
			2. Do 'Footer' > 'Visit' item verification
		""")

		allure.dynamic.title("'Footer' > Visit us item test")
		self.verify_footer_visit_item()
