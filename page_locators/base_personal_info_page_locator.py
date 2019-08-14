#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By
from expected_results.page_content.base_personal_info_content import BasePersonalInfoContent


class BasePersonalInfoPageLocator:
	'''
	Holds all shared locators for 'Register' and 'Forgot Login Info' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	'''

	HEADER = (By.XPATH, '//*[@id="rightPanel"]/h1[@class="title"]')
	DESCRIPTION = (By.XPATH, '//*[@id="rightPanel"]/p')

	FIRST_NAME_TITLE = (By.XPATH,
	                    '//*[contains(text(), "{}")]'.
	                    format(BasePersonalInfoContent.FORM['first name']['title']))
	FIRST_NAME_INPUT = (By.XPATH, '//*[contains(@id, "firstName")]')
	FIRST_NAME_ERROR = (By.XPATH, '//*[contains(@id, "firstName.errors")]')

	LAST_NAME_TITLE = (By.XPATH,
	                   '//*[contains(text(), "{}")]'.
	                   format(BasePersonalInfoContent.FORM['last name']['title']))
	LAST_NAME_INPUT = (By.XPATH, '//*[contains(@id, "lastName")]')
	LAST_NAME_ERROR = (By.XPATH, '//*[contains(@id, "lastName.errors")]')

	ADDRESS_TITLE = (By.XPATH,
	                 '//*[contains(text(), "{}")]'.
	                 format(BasePersonalInfoContent.FORM['address']['title']))
	ADDRESS_INPUT = (By.XPATH, '//*[contains(@id, "address.street")]')
	ADDRESS_ERROR = (By.XPATH, '//*[contains(@id, "address.street.errors")]')

	CITY_TITLE = (By.XPATH,
	              '//*[contains(text(), "{}")]'.
	              format(BasePersonalInfoContent.FORM['city']['title']))
	CITY_INPUT = (By.XPATH, '//*[contains(@id, "address.city")]')
	CITY_ERROR = (By.XPATH, '//*[contains(@id, "address.city.errors")]')

	STATE_TITLE = (By.XPATH,
	               '//*[contains(text(), "{}")]'.
	               format(BasePersonalInfoContent.FORM['state']['title']))
	STATE_INPUT = (By.XPATH, '//*[contains(@id, "address.state")]')
	STATE_ERROR = (By.XPATH, '//*[contains(@id, "address.state.errors")]')

	ZIP_CODE_TITLE = (By.XPATH,
	                  '//*[contains(text(), "{}")]'.
	                  format(BasePersonalInfoContent.FORM['zip code']['title']))
	ZIP_CODE_INPUT = (By.XPATH, '//*[contains(@id, "address.zipCode")]')
	ZIP_CODE_ERROR = (By.XPATH, '//*[contains(@id, "address.zipCode.errors")]')

	PHONE_TITLE = (By.XPATH,
	               '//*[contains(text(), "{}")]'.
	               format(BasePersonalInfoContent.FORM['phone']['title']))
	PHONE_INPUT = (By.XPATH, '//*[contains(@id, "phoneNumber")]')

	SSN_TITLE = (By.XPATH,
	             '//*[contains(text(), "{}")]'.
	             format(BasePersonalInfoContent.FORM['ssn']['title']))
	SSN_INPUT = (By.XPATH, '//*[contains(@id, "ssn")]')
	SSN_ERROR = (By.XPATH, '//*[contains(@id, "ssn.errors")]')

