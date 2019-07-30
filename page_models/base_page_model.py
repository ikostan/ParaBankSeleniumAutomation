import selenium.webdriver
from utils.driver import Driver
from page_context.base_page_context import BasePageContext


class BasePageModel:
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = BasePageContext.URL

	def __init__(self, driver: Driver, implicit_wait_time: 0):
		self._driver = self._set_driver(driver)
		self._set_implicit_wait(implicit_wait_time)

	@staticmethod
	def _set_driver(driver: selenium.webdriver):
		'''
		Check if driver of type: selenium.webdriver
		:param driver:
		:return:
		'''
		if type(driver) != Driver:
			raise TypeError('ERROR: please instantiate selenium webdriver using custom Driver class.')

		if type(driver.get_driver()) != selenium.webdriver:
			raise TypeError('ERROR: driver must be of type SELENIUM.WEBDRIVER.')

		return driver.get_driver()

	def _set_implicit_wait(self, implicit_wait_time: int):
		'''
		The default value of time that can be set using Implicit wait is zero.
		Its unit is in seconds.
		Implicit wait remains associated with the web element until it gets destroyed.
		:param implicit_wait_time:
		:return:
		'''
		if type(implicit_wait_time) != int:
			raise TypeError('ERROR: wrong data type. Please set "implicit_wait_time" value as integer.')
		self._driver.implicitly_wait(implicit_wait_time)

	def go(self):
		'''
		Opens test web page
		:return:
		'''
		self.driver.get_page(self._url)
		self.driver.maximize_window()

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
