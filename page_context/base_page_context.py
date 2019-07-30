from selenium.webdriver.common.by import By
import selenium.webdriver


class BasePage:

	def __init__(self, driver: selenium.webdriver):
		self._driver = self._set_driver(driver)

	@property
	def driver(self):
		'''
		Returns Selenium webdriver object
		:return:
		'''
		return self._driver

	@property
	def title(self):
		'''
		Returns web page title
		:return:
		'''
		return self._driver.title

	@property
	def url(self):
		'''
		Returns current URL
		:return:
		'''
		return self._driver.current_url

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

