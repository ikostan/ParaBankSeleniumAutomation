#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator


class AboutPageLocator(BasePageLocator):
	'''
	Holds all relevant locators for 'ABOUT' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	'''

	DESCRIPTION_TITLE = (By.XPATH, '//*[@id="rightPanel"]/h1')

	FIRST_LINE = (By.XPATH, '//*[@id="rightPanel"]/p[1]')

	SECOND_LINE = (By.XPATH, '//*[@id="rightPanel"]/p[2]')

	THIRD_LINE = (By.XPATH, '//*[@id="rightPanel"]/p[3]')

	LINK = (By.XPATH, '//*[@id="rightPanel"]/p[3]/a')

