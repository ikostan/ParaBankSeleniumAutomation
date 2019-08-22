#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator
from expected_results.page_content.bill_pay_content import BillPayContent


class BillPayPageLocator(BasePageLocator):
	PAYEE_NAME_TITLE = (By.XPATH, '//b[contains(text(), \'{}\')]'.
	                    format(BillPayContent.FORM['payee name']['title']))
	PAYEE_NAME_INPUT = (By.XPATH, '//input[@name=\'payee.name\']')
	PAYEE_NAME_ERROR = (By.XPATH, ';-)')

	ADDRESS_TITLE = (By.XPATH,
	                 '//*[contains(text(), "{}")]'.
	                 format(BillPayContent.FORM['address']['title']))
	ADDRESS_INPUT = (By.XPATH, '//*[contains(@name, "payee.address.street")]')
	ADDRESS_ERROR = (By.XPATH, '//*[contains(@name, "address.street.errors")]')

	CITY_TITLE = (By.XPATH,
	              '//*[contains(text(), "{}")]'.
	              format(BillPayContent.FORM['city']['title']))
	CITY_INPUT = (By.XPATH, '//*[contains(@name, "payee.address.city")]')
	CITY_ERROR = (By.XPATH, '//*[contains(@name, "address.city.errors")]')

	STATE_TITLE = (By.XPATH,
	               '//*[contains(text(), "{}")]'.
	               format(BillPayContent.FORM['state']['title']))
	STATE_INPUT = (By.XPATH, '//*[contains(@name, "payee.address.state")]')
	STATE_ERROR = (By.XPATH, '//*[contains(@name, "address.state.errors")]')

	ZIP_CODE_TITLE = (By.XPATH,
	                  '//*[contains(text(), "{}")]'.
	                  format(BillPayContent.FORM['zip code']['title']))
	ZIP_CODE_INPUT = (By.XPATH, '//*[contains(@name, "payee.address.zipCode")]')
	ZIP_CODE_ERROR = (By.XPATH, '//*[contains(@name, "address.zipCode.errors")]')

	PHONE_TITLE = (By.XPATH,
	               '//*[contains(text(), "{}")]'.
	               format(BillPayContent.FORM['phone']['title']))
	PHONE_INPUT = (By.XPATH, '//*[contains(@name, "payee.phoneNumber")]')

	ACCOUNT_TITLE = (By.XPATH, '//b[contains(text(), \'{}\')]'.
	                 format(BillPayContent.FORM['account']['title']))
	ACCOUNT_INPUT = (By.XPATH, '//*[contains(@name, "payee.accountNumber")]')
	ACCOUNT_ERROR = (By.XPATH, '')

	VERIFY_ACCOUNT_TITLE = (By.XPATH, '//b[contains(text(), \'{}\')]'.
	                        format(BillPayContent.FORM['verify account']['title']))
	VERIFY_ACCOUNT_INPUT = (By.XPATH, '//*[contains(@name, "verifyAccount")]')
	VERIFY_ACCOUNT_ERROR = (By.XPATH, '')

	AMOUNT_TITLE = (By.XPATH, '//b[contains(text(), \'{}\')]'.
	                format(BillPayContent.FORM['amount']['title']))
	AMOUNT_INPUT = (By.XPATH, '//*[contains(@name, "amount")]')
	AMOUNT_ERROR = (By.XPATH, '')

	FROM_ACCOUNT_TITLE = (By.XPATH, '//b[contains(text(), \'{}\')]'.
	                      format(BillPayContent.FORM['from account']['title']))
	FROM_ACCOUNT_SELECT = (By.XPATH, '//*[contains(@name, "fromAccountId")]')
	FROM_ACCOUNT_ERROR = (By.XPATH, '')

	SEND_PAYMENT_BUTTON = (By.XPATH, '//input[contains(@value, \'{}\')]'.
	                       format(BillPayContent.SEND_PAYMENT_BUTTON['input']['value']))

	BILL_PAYMENT_COMPLETE_TITLE = (By.XPATH, '//h1[contains(text(), \'{}\')]'.
	                               format(BillPayContent.BILL_PAYMENT_COMPLETE_TITLE))

	PAYMENT_MESSAGE = (By.XPATH, '//p[contains(text(), \'Bill Payment to \')]')

	MORE_DETAILS_MESSAGE = (By.XPATH, '//p[contains(text(), \'{}\')]'.
	                        format(BillPayContent.MORE_DETAILS_MESSAGE))
