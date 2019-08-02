from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator


class HomePageLocator(BasePageLocator):
	'''
	Holds all relevant locators for 'HOME' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	'''

	# ATM Services
	ATM_SERVICES_TITLE = (By.XPATH, '//*[@id="rightPanel"]/'
	                                'ul[contains(@class, "services")]/'
	                                'li[contains(@class, "captionone")]')

	WITHDRAW_FUNDS = (By.XPATH, '//*[@id="rightPanel"]/'
	                            'ul[contains(@class, "services")]/'
	                            'li[2]/a')

	ATM_TRANSFER_FUNDS = (By.XPATH, '//*[@id="rightPanel"]/'
	                                'ul[contains(@class, "services")]/'
	                                'li[3]/a')

	CHECK_BALANCES = (By.XPATH, '//*[@id="rightPanel"]/'
	                            'ul[contains(@class, "services")]/'
	                            'li[4]/a')

	MAKE_DEPOSITS = (By.XPATH, '//*[@id="rightPanel"]/'
	                           'ul[contains(@class, "services")]/'
	                           'li[5]/a')

	# Online Services
	ONLINE_SERVICES_TITLE = (By.XPATH, '//*[@id="rightPanel"]/'
	                                   'ul[contains(@class, "servicestwo")]/'
	                                   'li[contains(@class, "captiontwo")]')

	BILL_PAY = (By.XPATH, '//*[@id="rightPanel"]/'
	                      'ul[contains(@class, "servicestwo")]/'
	                      'li[2]/a')

	ACCOUNT_HISTORY = (By.XPATH, '//*[@id="rightPanel"]/'
	                             'ul[contains(@class, "servicestwo")]/'
	                             'li[3]/a')

	ONLINE_TRANSFER_FUNDS = (By.XPATH, '//*[@id="rightPanel"]/'
	                                   'ul[contains(@class, "servicestwo")]/'
	                                   'li[4]/a')

	READ_MORE_SERVICES = (By.XPATH, '//*[@id="rightPanel"]/p[1]/a')

	# News Section
	LATEST_NEWS = (By.XPATH, '//*[@id="rightPanel"]/h4')

	READ_MORE_NEWS = (By.XPATH, '//*[@id="rightPanel"]/p[2]/a')

