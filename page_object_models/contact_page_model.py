#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.common.exceptions import NoSuchElementException

from element_object_models.element import Element
from page_object_models.base_page_model import BasePageModel
from page_locators.contact_page_locator import ContactPageLocator
from expected_results.page_content.contact_page_content import ContactPageContent


class ContactPageModel(BasePageModel):
	"""
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the
	test code and technical implementation is created.
	"""

	_url = ContactPageContent.URL

	def send_btn_label(self):
		"""
		Returns "SEND TO CUSTOMER CARE" button label
		:return:
		"""

		element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.SEND_BUTTON)
		txt = element.element_value
		return txt

	def click_send_btn(self):
		"""
		Click on "FIND MY LOGIN INFO" button
		:return:
		"""

		element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.SEND_BUTTON)
		element.press_button()
		return None

	def type_name(self, value: str):
		"""
		Type Name value
		Returns None.
		:return:
		"""

		element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.NAME_INPUT)
		element.write(value)
		return None

	def name_title(self):
		"""
		Returns Name Title
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.NAME_TITLE)
			txt = element.text
			return txt
		except NoSuchElementException:
			return None

	def name_field(self):
		"""
		Returns Name Field value
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.NAME_INPUT)
			txt = element.element_value
			return txt
		except NoSuchElementException:
			return None

	def name_error(self):
		"""
		Returns Name Error
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.NAME_ERROR)
			txt = element.text
			return txt
		except NoSuchElementException:
			return None

	def type_email(self, value: str):
		"""
		Type Email value
		Returns None.
		:return:
		"""

		element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.EMAIL_INPUT)
		element.write(value)
		return None

	def email_title(self):
		"""
		Returns Email Title
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.EMAIL_TITLE)
			txt = element.text
			return txt
		except NoSuchElementException:
			return None

	def email_field(self):
		"""
		Returns Email Field value
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.EMAIL_INPUT)
			txt = element.element_value
			return txt
		except NoSuchElementException:
			return None

	def email_error(self):
		"""
		Returns Email Error
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.EMAIL_ERROR)
			txt = element.text
			return txt
		except NoSuchElementException:
			return None

	def type_phone(self, value: str):
		"""
		Type Phone value
		Returns None.
		:return:
		"""

		element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.PHONE_INPUT)
		element.write(value)
		return None

	def phone_title(self):
		"""
		Returns PHONE Title
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.PHONE_TITLE)
			txt = element.text
			return txt
		except NoSuchElementException:
			return None

	def phone_field(self):
		"""
		Returns Phone Field value
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.PHONE_INPUT)
			txt = element.element_value
			return txt
		except NoSuchElementException:
			return None

	def phone_error(self):
		"""
		Returns Phone Error
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.PHONE_ERROR)
			txt = element.text
			return txt
		except NoSuchElementException:
			return None

	def type_message(self, value: str):
		"""
		Type Message value
		Returns None.
		:return:
		"""

		element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.MESSAGE_INPUT)
		element.write(value)
		return None

	def message_title(self):
		"""
		Returns Message Title
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.MESSAGE_TITLE)
			txt = element.text
			return txt
		except NoSuchElementException:
			return None

	def message_field(self):
		"""
		Returns Message Field value
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.MESSAGE_INPUT)
			txt = element.element_value
			return txt
		except NoSuchElementException:
			return None

	def message_error(self):
		"""
		Returns Message Error
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.MESSAGE_ERROR)
			txt = element.text
			return txt
		except NoSuchElementException:
			return None

	def thank_you_message(self):
		"""
		Returns 'Thank you...' message value
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.THANK_YOU)
			txt = element.text
			return txt
		except NoSuchElementException:
			return None

	def success_message(self):
		"""
		Returns 'Success' message value
		Returns None in case of failure.
		:return:
		"""
		try:
			element = Element(self.driver, self.explicit_wait_time, ContactPageLocator.SUCCESS_MESSAGE)
			txt = element.text
			return txt
		except NoSuchElementException:
			return None
