from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator


class AdminPageLocator(BasePageLocator):
	'''
	Holds all relevant locators for 'Admin' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	'''

	INITIALIZE_BUTTON = (By.XPATH, '//button[contains(text(),\'Initialize\')]')

	CLEAN_BUTTON = (By.XPATH, '//button[contains(text(),\'Clean\')]')
