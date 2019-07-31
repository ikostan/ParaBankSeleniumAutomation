import unittest


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
		cls.driver = None

	def setUp(self):
		if self.driver is not None:
			self.driver.quit()
		self.driver = None

	@classmethod
	def tearDownClass(cls):
		if cls.page:
			cls.page.quit()

	def tearDown(self):
		if self.page:
			self.page.close()


if __name__ == '__main__':
	unittest.main()
