import selenium.webdriver


class BasePageModel:
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	def __init__(self, driver: selenium.webdriver, implicit_wait_time: 0):

		if type(implicit_wait_time) != int:
			raise TypeError('ERROR: wrong data type. Please set "implicit_wait_time" value as integer.')

		self._driver = self._set_driver(driver)

		# The default value of time that can be set using Implicit wait is zero.
		# Its unit is in seconds.
		# Implicit wait remains associated with the web element until it gets destroyed.
		self._driver.implicitly_wait(implicit_wait_time)

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
