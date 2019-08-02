from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator


class HomePageLocator(BasePageLocator):
	'''
	Holds all relevant locators for 'HOME' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	'''

	ATM_SERVICES_TITLE = (By.XPATH, '//*[@id="rightPanel"]/'
	                                'ul[contains(@class, "services")]/'
	                                'li[contains(@class, "captionone")]')

	WITHDRAW_FUNDS = (By.XPATH, '//*[@id="rightPanel"]/'
	                            'ul[contains(@class, "services")]/'
	                            'li[2]/a')

	TRANSFER_FUNDS = (By.XPATH, '//*[@id="rightPanel"]/'
	                            'ul[contains(@class, "services")]/'
	                            'li[3]/a')

	CHECK_BALANCES = (By.XPATH, '//*[@id="rightPanel"]/'
	                            'ul[contains(@class, "services")]/'
	                            'li[4]/a')

	MAKE_DEPOSITS = (By.XPATH, '//*[@id="rightPanel"]/'
	                           'ul[contains(@class, "services")]/'
	                           'li[5]/a')

