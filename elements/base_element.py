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
		if type(driver) != selenium.webdriver:
			raise TypeError('ERROR: driver must be of type SELENIUM.WEBDRIVER')
		return driver

	@staticmethod
	def _set_locator(locator: tuple):
		'''
		Check if locator of type: tuple
		:param locator:
		:return:
		'''
		if type(locator) != tuple:
			raise TypeError('ERROR: locator must be of type TUPLE')
		return locator
