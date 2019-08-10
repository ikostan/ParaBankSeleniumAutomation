#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from elements.element import Element
from page_models.base_page_model import BasePageModel
from page_locators.base_personal_info_page_locator import BasePersonalInfoPageLocator


class BasePersonalInfoPageModel(BasePageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	@property
	def header(self):
		'''
		Returns header text
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.HEADER)
		txt = element.text
		return txt

	@property
	def description(self):
		'''
		Returns description text
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.DESCRIPTION)
		txt = element.text
		return txt

	@property
	def first_name_title(self):
		'''
		Returns first name title text
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.FIRST_NAME_TITLE)
		txt = element.text
		return txt

	def type_first_name(self, first_name: str):
		'''
		Write text into first name input field
		:param first_name:
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.FIRST_NAME_INPUT)
		element.write(first_name)
		return None

	@property
	def first_name(self):
		'''
		Returns first name input field value
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.FIRST_NAME_INPUT)
		value = element.element_value
		return value

	@property
	def last_name_title(self):
		'''
		Returns last name title text
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.LAST_NAME_TITLE)
		txt = element.text
		return txt

	def type_last_name(self, last_name: str):
		'''
		Write text into last name input field
		:param last_name:
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.LAST_NAME_INPUT)
		element.write(last_name)
		return None

	@property
	def last_name(self):
		'''
		Returns last name input field value
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.LAST_NAME_INPUT)
		value = element.element_value
		return value

	@property
	def address_title(self):
		'''
		Returns address title text
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.ADDRESS_TITLE)
		txt = element.text
		return txt

	def type_address(self, address: str):
		'''
		Write text into address input field
		:param address:
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.ADDRESS_INPUT)
		element.write(address)
		return None

	@property
	def address(self):
		'''
		Returns address input field value
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.ADDRESS_INPUT)
		value = element.element_value
		return value

	@property
	def city_title(self):
		'''
		Returns address title text
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.CITY_TITLE)
		txt = element.text
		return txt

	def type_city(self, city: str):
		'''
		Write text into city input field
		:param city:
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.CITY_INPUT)
		element.write(city)
		return None

	@property
	def city(self):
		'''
		Returns city input field value
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.CITY_INPUT)
		value = element.element_value
		return value

	@property
	def state_title(self):
		'''
		Returns state title text
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.STATE_TITLE)
		txt = element.text
		return txt

	def type_state(self, state: str):
		'''
		Write text into state input field
		:param state:
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.STATE_INPUT)
		element.write(state)
		return None

	@property
	def state(self):
		'''
		Returns state input field value
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.STATE_INPUT)
		value = element.element_value
		return value

	@property
	def zip_code_title(self):
		'''
		Returns zip code title text
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.ZIP_CODE_TITLE)
		txt = element.text
		return txt

	def type_zip_code(self, zip_code: str):
		'''
		Write text into zip_code input field
		:param zip_code:
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.ZIP_CODE_INPUT)
		element.write(zip_code)
		return None

	@property
	def zip_code(self):
		'''
		Returns zip code input field value
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.ZIP_CODE_INPUT)
		value = element.element_value
		return value

	@property
	def phone_title(self):
		'''
		Returns phone title text
		:return:
		'''

		element = Element(self.driver,
		                  self.explicit_wait_time,
		                  BasePersonalInfoPageLocator.PHONE_TITLE)
		txt = element.text
		return txt

	def type_phone(self, phone_number: str):
		'''
		Write text into phone input field
		:param phone_number:
		:return:
		'''

		element = Element(self.driver,
		                  self.explicit_wait_time,
		                  BasePersonalInfoPageLocator.PHONE_INPUT)
		element.write(phone_number)
		return None

	@property
	def phone(self):
		'''
		Returns phone input field value
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.PHONE_INPUT)
		value = element.element_value
		return value

	@property
	def ssn_title(self):
		'''
		Returns SSN title text
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.SSN_TITLE)
		txt = element.text
		return txt

	def type_ssn(self, ssn: str):
		'''
		Write text into ssn input field
		:param ssn:
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.SSN_INPUT)
		element.write(ssn)
		return None

	@property
	def ssn(self):
		'''
		Returns SSN input field value
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, BasePersonalInfoPageLocator.SSN_INPUT)
		value = element.element_value
		return value
