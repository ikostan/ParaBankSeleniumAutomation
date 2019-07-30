import unittest
from utils.driver import Driver
from page_models.home_page_model import HomePageModel


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
		self.assertEqual(True, False)

	@classmethod
	def tearDownClass(cls):
		cls.page.quit()

	def tearDown(self):
		self.driver.stop_client()
		self.driver.close()


if __name__ == '__main__':
	unittest.main()
