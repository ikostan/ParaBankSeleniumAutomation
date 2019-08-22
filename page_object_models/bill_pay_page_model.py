#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from tests.config import Config
from utils.driver import Driver

from element_object_models.element import Element
from page_object_models.base_page_model import BasePageModel
from page_locators.bill_pay_page_locator import BillPayPageLocator
from expected_results.page_content.bill_pay_content import BillPayContent


class BillPayPageModel(BasePageModel):

	def __init__(self, config: Config, driver: Driver, implicit_wait_time, explicit_wait_time):
		super().__init__(config, driver, implicit_wait_time, explicit_wait_time)
		_url = config.base_url + BillPayContent.URL

	def fill_out_bill_payment_form(self, payee, account, amount):
		"""
		Fill out 'Bill Payment Service' form.
		Verify data from every field (compare expected vs actual value).
		:param account:
		:param amount:
		:param payee:
		:return:
		"""

		# 1 Payee Name:
		payee_full_name = payee.FIRST_NAME + " " + payee.LAST_NAME
		self.type_payee_name(payee_full_name)
		with allure.step("Verify payee name"):
			print('payee name: {}'.format(payee_full_name))
			assert payee_full_name == self.payee_name()

		# 2 Address:
		self.type_address(payee.ADDRESS)
		with allure.step("Verify payee address"):
			print('payee address: {}'.format(payee.ADDRESS))
			assert payee.ADDRESS == self.address()

		# 3 City:
		self.type_city(payee.CITY)
		with allure.step("Verify payee city"):
			print('payee city: {}'.format(payee.CITY))
			assert payee.CITY == self.city()

		# 4 State:
		self.type_state(payee.STATE)
		with allure.step("Verify payee state"):
			print('payee state: {}'.format(payee.STATE))
			assert payee.STATE == self.state()

		# 5 Zip Code:
		self.type_zip_code(payee.ZIP_CODE)
		with allure.step("Verify payee zip code"):
			print('payee zip code: {}'.format(payee.ZIP_CODE))
			assert payee.ZIP_CODE == self.zip_code()

		# 6 Phone:
		self.type_phone(payee.PHONE)
		with allure.step("Verify payee phone"):
			print('payee phone: {}'.format(payee.PHONE))
			assert payee.PHONE == self.phone()

		# 7 Account:
		self.type_account(account)
		with allure.step("Verify payee account"):
			print('payee account: {}'.format(account))
			assert account == self.account()

		# 8 Verify Account:
		self.type_verify_account(account)
		with allure.step("Verify 'Verify Account'"):
			assert account == self.verify_account()

		# 9 Amount
		self.type_amount(amount)
		with allure.step("Verify amount"):
			print('payment amount: {}'.format(amount))
			assert amount == self.amount()

		return None

	def type_payee_name(self, name):
		"""
		Type payee name into "Payee Name" field
		Raise NoSuchElementException on failure
		:param name:
		:return:
		"""

		with allure.step("Type payee name"):
			element = Element(driver=self.driver,
			                  explicit_wait_time=self.explicit_wait_time,
			                  locator=BillPayPageLocator.PAYEE_NAME_INPUT)
			element.write(name)
			return None

	def payee_name(self):
		"""
		Get payee name from "Payee Name" field
		Raise NoSuchElementException on failure
		:param:
		:return:
		"""

		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=BillPayPageLocator.PAYEE_NAME_INPUT)
		return element.element_value

	def type_address(self, address):
		"""
		Type payee address into "Address" field
		Raise NoSuchElementException on failure
		:param address:
		:return:
		"""

		with allure.step("Type payee address"):
			element = Element(driver=self.driver,
			                  explicit_wait_time=self.explicit_wait_time,
			                  locator=BillPayPageLocator.ADDRESS_INPUT)
			element.write(address)
			return None

	def address(self):
		"""
		Get payee address from "Address" field
		Raise NoSuchElementException on failure
		:param:
		:return:
		"""

		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=BillPayPageLocator.ADDRESS_INPUT)
		return element.element_value

	def type_city(self, city):
		"""
		Type city into "City" field
		Raise NoSuchElementException on failure
		:param city:
		:return:
		"""

		with allure.step("Type payee city"):
			element = Element(driver=self.driver,
			                  explicit_wait_time=self.explicit_wait_time,
			                  locator=BillPayPageLocator.CITY_INPUT)
			element.write(city)
			return None

	def city(self):
		"""
		Get payee city from "City" field
		Raise NoSuchElementException on failure
		:param:
		:return:
		"""
		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=BillPayPageLocator.CITY_INPUT)
		return element.element_value

	def type_state(self, state):
		"""
		Type state into "Sate" field
		Raise NoSuchElementException on failure
		:param state:
		:return:
		"""

		with allure.step("Type payee state"):
			element = Element(driver=self.driver,
			                  explicit_wait_time=self.explicit_wait_time,
			                  locator=BillPayPageLocator.STATE_INPUT)
			element.write(state)
			return None

	def state(self):
		"""
		Get payee state from "State" field
		Raise NoSuchElementException on failure
		:param:
		:return:
		"""

		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=BillPayPageLocator.STATE_INPUT)
		return element.element_value

	def type_zip_code(self, zip_code):
		"""
		Type zip code into "Zip Code" field
		Raise NoSuchElementException on failure
		:param zip_code:
		:return:
		"""

		with allure.step("Type payee zip code"):
			element = Element(driver=self.driver,
			                  explicit_wait_time=self.explicit_wait_time,
			                  locator=BillPayPageLocator.ZIP_CODE_INPUT)
			element.write(zip_code)
			return None

	def zip_code(self):
		"""
		Get payee zip code from "Zip Code" field
		Raise NoSuchElementException on failure
		:param:
		:return:
		"""

		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=BillPayPageLocator.ZIP_CODE_INPUT)
		return element.element_value

	def type_phone(self, phone):
		"""
		Type payee phone into "Phone" field
		Raise NoSuchElementException on failure
		:param phone:
		:return:
		"""

		with allure.step("Type payee phone"):
			element = Element(driver=self.driver,
			                  explicit_wait_time=self.explicit_wait_time,
			                  locator=BillPayPageLocator.PHONE_INPUT)
			element.write(phone)
			return None

	def phone(self):
		"""
		Get payee phone from "Phone" field
		Raise NoSuchElementException on failure
		:param:
		:return:
		"""

		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=BillPayPageLocator.PHONE_INPUT)
		return element.element_value

	def type_account(self, account):
		"""
		Type account number into "Account" field
		Raise NoSuchElementException on failure
		:param account:
		:return:
		"""

		with allure.step("Type payee account"):
			element = Element(driver=self.driver,
			                  explicit_wait_time=self.explicit_wait_time,
			                  locator=BillPayPageLocator.ACCOUNT_INPUT)
			element.write(account)
			return None

	def account(self):
		"""
		Get payee account from "Account" field
		Raise NoSuchElementException on failure
		:param:
		:return:
		"""

		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=BillPayPageLocator.ACCOUNT_INPUT)
		return element.element_value

	def type_verify_account(self, account):
		"""
		Type account number into "Verify Account" field
		Raise NoSuchElementException on failure
		:param account:
		:return:
		"""

		with allure.step("Type verify address"):
			element = Element(driver=self.driver,
			                  explicit_wait_time=self.explicit_wait_time,
			                  locator=BillPayPageLocator.VERIFY_ACCOUNT_INPUT)
			element.write(account)
			return None

	def verify_account(self):
		"""
		Get verify account value from "Verify Account" field
		Raise NoSuchElementException on failure
		:param:
		:return:
		"""

		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=BillPayPageLocator.VERIFY_ACCOUNT_INPUT)
		return element.element_value

	def type_amount(self, amount):
		"""
		Type amount into "Amount" field
		Raise NoSuchElementException on failure
		:param amount:
		:return:
		"""

		with allure.step("Type amount"):
			element = Element(driver=self.driver,
			                  explicit_wait_time=self.explicit_wait_time,
			                  locator=BillPayPageLocator.AMOUNT_INPUT)
			element.write(amount)
			return None

	def amount(self):
		"""
		Get amount value from "Amount" field
		Raise NoSuchElementException on failure
		:param:
		:return:
		"""

		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=BillPayPageLocator.AMOUNT_INPUT)
		return element.element_value

	def hit_send_payment_button(self):
		"""
		Click on "Send Payment" button
		Raise NoSuchElementException on failure
		:param:
		:return:
		"""
		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=BillPayPageLocator.SEND_PAYMENT_BUTTON)
		element.press_button()
		return None

	def bill_payment_complete_title(self):
		"""
		Returns Bill Payment Complete title.
		Returns NoSuchElementException on failure.
		:return:
		"""
		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=BillPayPageLocator.BILL_PAYMENT_COMPLETE_TITLE)
		return element.text

	def payment_message(self):
		"""
		Returns Bill Payment Complete title.
		Returns NoSuchElementException on failure.
		:return:
		"""
		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=BillPayPageLocator.PAYMENT_MESSAGE)
		return element.text

	def more_details_message(self):
		"""
		Returns Bill Payment Complete title.
		Returns NoSuchElementException on failure.
		:return:
		"""
		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=BillPayPageLocator.MORE_DETAILS_MESSAGE)
		return element.text


