import selenium.webdriver


class BaseElement:

	def __init__(self, driver: selenium.webdriver, locator=None):
		self._driver = self._set_driver(driver)
		self._locator = self._set_locator(locator)

	@property
	def driver(self):
		'''
		Returns selenium.webdriver object
		:return:
		'''
		return self._driver

	@property
	def locator(self):
		'''
		Returns locator object (tuple)
		:return:
		'''
		return self._locator

	@staticmethod
	def _set_driver(driver: selenium.webdriver):
		'''
		Check if driver of type: selenium.webdriver
		:param driver:
		:return:
		'''
		BaseElement._check_driver_type(driver)
		return driver

	@staticmethod
	def _check_driver_type(driver):

		# print('\nDRIVER TYPE: {}, {}\n'.format(type(driver), driver.capabilities['browserName']))  # Debug only
		if driver.capabilities['browserName'] == 'chrome':
			if type(driver) != selenium.webdriver.chrome.webdriver.WebDriver:
				raise TypeError('\nERROR: driver must be of type "selenium.webdriver.chrome.webdriver.WebDriver"\n')
			return None

		if driver.capabilities['browserName'] == 'mozilla':
			if type(driver) != selenium.webdriver.firefox.webdriver.WebDriver:
				raise TypeError('\nERROR: driver must be of type "selenium.webdriver.firefox.webdriver.WebDriver"\n')
			return None

		if driver.capabilities['browserName'] == 'edge':
			if type(driver) != selenium.webdriver.edge.webdriver.WebDriver:
				raise TypeError('\nERROR: driver must be of type "selenium.webdriver.edge.webdriver.WebDriver"\n')
			return None

		raise TypeError('\nERROR: unsupported webdriver type\n')

	@staticmethod
	def _set_locator(locator: tuple):
		'''
		Check if locator of type: tuple
		:param locator:
		:return:
		'''
		if type(locator) != tuple:
			raise TypeError('\nERROR: locator must be of type TUPLE\n')
		return locator
