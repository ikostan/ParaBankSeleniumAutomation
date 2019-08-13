#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


class BaseUser:

	def __init__(self, user_template):

		self._first_name = user_template.FIRST_NAME
		self._last_name = user_template.LAST_NAME

		self._address = user_template.ADDRESS
		self._city = user_template.CITY
		self._state = user_template.STATE
		self._zip_code = user_template.ZIP_CODE
		self._phone = user_template.PHONE

		self._username = user_template.USERNAME
		self._password = user_template.PASSWORD

		self._ssn = user_template.SSN

		self._init_balance = user_template.INIT_BALANCE
		self._min_balance = user_template.MIN_BALANCE

		self._print_user_data()

	def _print_user_data(self):
		'''
		Print all user data fields
		:return:
		'''

		print('First Name: {}\n'
		      'Last Name: {}\n'
		      'Address: {}\n'
		      'City: {}\n'
		      'State: {}\n'
		      'Zip Code: {}\n'
		      'Phone #: {}\n'
		      'SSN: {}\n'
		      'Username: {}\n'
		      'Password: {}\n'.format(self.first_name,
		                              self.last_name,
		                              self.address,
		                              self.city,
		                              self.state,
		                              self.zip_code,
		                              self.phone,
		                              self.ssn,
		                              self.username,
		                              self.password))

	@property
	def first_name(self):
		'''
		Returns first name value
		:return:
		'''
		return self._first_name

	@property
	def last_name(self):
		'''
		Returns first name value
		:return:
		'''
		return self._last_name

	@property
	def address(self):
		'''
		Returns address value
		:return:
		'''
		return self._address

	@property
	def city(self):
		'''
		Returns city value
		:return:
		'''
		return self._city

	@property
	def state(self):
		'''
		Returns state value
		:return:
		'''
		return self._state

	@property
	def zip_code(self):
		'''
		Returns zip code value
		:return:
		'''
		return self._zip_code

	@property
	def phone(self):
		'''
		Returns phone value
		:return:
		'''
		return self._phone

	@property
	def ssn(self):
		'''
		Returns ssn value
		:return:
		'''
		return self._ssn

	@property
	def username(self):
		'''
		Returns username value
		:return:
		'''
		return self._username

	@property
	def password(self):
		'''
		Returns password value
		:return:
		'''
		return self._password

