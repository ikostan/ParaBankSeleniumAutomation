#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator


class LoginPageLocator(BasePageLocator):
	'''
	Holds all relevant locators for 'Login' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	'''

	ERROR_TITLE = (By.XPATH, '//*[@id="rightPanel"]/h1')
	ERROR_MESSAGE = (By.XPATH, '//*[@id="rightPanel"]/p')
