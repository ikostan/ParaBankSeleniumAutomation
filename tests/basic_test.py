import unittest
from utils.driver import Driver
from page_models.home_page_model import HomePageModel
from page_context.home_page_context import HomePageContext


class MyTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.page = None
		cls.driver = None

	def setUp(self):
		if self.driver is not None:
			self.driver.quit()

		self.driver = None

	def test_something(self):
		browser = 'chrome'
		self.driver = Driver(browser)
		self.page = HomePageModel(self.driver)
		self.page.go()
		self.assertEqual(HomePageContext.TITLE, self.page.title)

	@classmethod
	def tearDownClass(cls):
		if cls.page:
			cls.page.quit()

	def tearDown(self):
		self.page.close()


if __name__ == '__main__':
	unittest.main()
