import unittest
from utils.screenshot import screenshots_collector
from page_context.base_page_context import BasePageContext


class BaseTestCase(unittest.TestCase):
	"""
	BaseTest
	This class should be the parent class to each unit test.
	It allows for instantiation of the database dynamically,
	and makes sure that it is a new, blank database each time.
	"""

	@classmethod
	def setUpClass(cls):
		cls.page = None

	def setUp(self):
		if self.page is not None:
			self.page.quit()
		self.page = None

	@classmethod
	def tearDownClass(cls):
		if cls.page:
			cls.page.quit()

	def tearDown(self):
		screenshots_collector()
		if self.page:
			self.page.close()

	def verify_solutions_menu_items(self):
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Solutions']['text'],
		                 self.page.solutions_menu_text)
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Solutions']['class'],
		                 self.page.solutions_menu_class)

		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['About Us']['href'],
		                 self.page.about_us_menu_item_formated_href)
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['About Us']['text'],
		                 self.page.about_us_menu_item_text)

		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Services']['href'],
		                 self.page.services_us_menu_item_formated_href)
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Services']['text'],
		                 self.page.services_us_menu_item_text)

		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Products']['href'],
		                 self.page.products_menu_item_formated_href)
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Products']['text'],
		                 self.page.products_menu_item_text)

		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Locations']['href'],
		                 self.page.locations_menu_item_formated_href)
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Locations']['text'],
		                 self.page.locations_menu_item_text)

		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Admin Page']['href'],
		                 self.page.admin_page_menu_item_formated_href)
		self.assertEqual(BasePageContext.LEFT_MENU_ITEMS['Admin Page']['text'],
		                 self.page.admin_page_menu_item_text)

	def verify_right_menu_buttons(self):
		self.assertEqual(BasePageContext.MENU_BUTTONS['home']['href'],
		                 self.page.home_button_formated_href)
		self.assertEqual(BasePageContext.MENU_BUTTONS['home']['text'],
		                 self.page.home_button_text)

		self.assertEqual(BasePageContext.MENU_BUTTONS['about']['href'],
		                 self.page.about_button_formated_href)
		self.assertEqual(BasePageContext.MENU_BUTTONS['about']['text'],
		                 self.page.about_button_text)

		self.assertEqual(BasePageContext.MENU_BUTTONS['contact']['href'],
		                 self.page.contact_button_formated_href)
		self.assertEqual(BasePageContext.MENU_BUTTONS['contact']['text'],
		                 self.page.contact_button_text)

	def verify_parabank_logo(self):
		self.assertEqual(BasePageContext.SLOGAN,
		                 self.page.slogan)
		self.assertEqual(BasePageContext.PARA_BANK_LOGO['href'],
		                 self.page.para_bank_logo_formated_href)
		self.assertEqual(BasePageContext.PARA_BANK_LOGO['class'],
		                 self.page.para_bank_logo_img_class)
		self.assertEqual(BasePageContext.PARA_BANK_LOGO['src'],
		                 self.page.para_bank_logo_formated_img_src)
		self.assertEqual(BasePageContext.PARA_BANK_LOGO['alt'],
		                 self.page.para_bank_logo_img_alt)
		self.assertEqual(BasePageContext.PARA_BANK_LOGO['title'],
		                 self.page.para_bank_logo_img_title)

	def verify_parabank_admin_logo(self):
		self.assertEqual(BasePageContext.ADMIN_LOGO['href'],
		                 self.page.admin_logo_formated_href)
		self.assertEqual(BasePageContext.ADMIN_LOGO['class'],
		                 self.page.admin_logo_img_class)
		self.assertEqual(BasePageContext.ADMIN_LOGO['src'],
		                 self.page.admin_logo_formated_img_src)


if __name__ == '__main__':
	unittest.main()
