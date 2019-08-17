#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By

from expected_results.page_content.contact_page_content import ContactPageContent
from page_locators.base_page_locator import BasePageLocator


class ContactPageLocator(BasePageLocator):
	"""
	Holds all relevant locators for 'Contact' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	"""

	NAME_TITLE = (By.XPATH, '//b[@innertext=\'{}\']'.format(ContactPageContent.CONTACT_FORM['name']['title']))
	NAME_INPUT = (By.XPATH, '/html//input[@id=\'{}\']'.format(ContactPageContent.CONTACT_FORM['name']['id']))
	NAME_ERROR = (By.XPATH, '/html//span[@id=\'name.errors\']')  # /html//span[@id='name.errors']

	EMAIL_TITLE = (By.XPATH, '//b[@innertext=\'{}\']'.format(ContactPageContent.CONTACT_FORM['email']['title']))
	EMAIL_INPUT = (By.XPATH, '/html//input[@id=\'{}\']'.format(ContactPageContent.CONTACT_FORM['email']['id']))
	EMAIL_ERROR = (By.XPATH, '/html//span[@id=\'email.errors\']')

	PHONE_TITLE = (By.XPATH, '//b[@innertext=\'Phone:\']'.format(ContactPageContent.CONTACT_FORM['phone']['title']))
	PHONE_INPUT = (By.XPATH, '/html//input[@id=\'{}\']'.format(ContactPageContent.CONTACT_FORM['phone']['id']))
	PHONE_ERROR = (By.XPATH, '/html//span[@id=\'phone.errors\']')

	MESSAGE_TITLE = (By.XPATH, '///b[@innertext=\'Message:\']'.format(ContactPageContent.CONTACT_FORM['message']['title']))
	MESSAGE_INPUT = (By.XPATH, '/html//textarea[@id=\'{}\']'.format(ContactPageContent.CONTACT_FORM['message']['id']))
	MESSAGE_ERROR = (By.XPATH, '/html//span[@id=\'message.errors\']')

	SEND_BUTTON = (By.XPATH, '//input[@value=\'{}\']'.format(ContactPageContent.CONTACT_FORM['button']['value']))

	THANK_YOU = (By.XPATH, '//p[contains(text(), "Thank you ")]')
	SUCCESS_MESSAGE = (By.XPATH, '//p[contains(text(), "A Customer Care Representative")]')

