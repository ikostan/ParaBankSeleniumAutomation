#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


class BaseUser:

	def __init__(self, user_template):

		self._first_name = user_template.FIRST_NAME
		self._last_name = user_template.LAST_NAME

		self.address = user_template.ADDRESS
		self.city = user_template.CITY
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
		"""
		Returns first name value
		:return:
		"""
		return self._first_name

	@first_name.setter
	def first_name(self, name: str):
		"""
		Set first name value
		:param name:
		:return:
		"""
		self._first_name = name

	@property
	def last_name(self):
		"""
		Returns first name value
		:return:
		"""
		return self._last_name

	@last_name.setter
	def last_name(self, name: str):
		"""
		Set first name value
		:param name:
		:return:
		"""
		self._last_name = name

	@property
	def address(self):
		"""
		Returns address value
		:return:
		"""
		return self._address

	@address.setter
	def address(self, address: str):
		"""
		Set address value
		:param address:
		:return:
		"""
		self._address = address

	@property
	def city(self):
		"""
		Returns city value
		:return:
		"""
		return self._city

	@city.setter
	def city(self, city: str):
		"""
		Set city value
		:param city:
		:return:
		"""
		self._city = city

	@property
	def state(self):
		"""
		Returns state value
		:return:
		"""
		return self._state

	@state.setter
	def state(self, state: str):
		"""
		Set state value
		:param state:
		:return:
		"""
		self._state = state

	@property
	def zip_code(self):
		"""
		Returns zip code value
		:return:
		"""
		return self._zip_code

	@zip_code.setter
	def zip_code(self, zip_code: str):
		"""
		Set zip code value
		:param zip_code:
		:return:
		"""
		self._zip_code = zip_code

	@property
	def phone(self):
		"""
		Returns phone value
		:return:
		"""
		return self._phone

	@phone.setter
	def phone(self, phone: str):
		"""
		Set phone value
		:param phone:
		:return:
		"""
		self._phone = phone

	@property
	def ssn(self):
		'''
		Returns ssn value
		:return:
		'''
		return self._ssn

	@ssn.setter
	def ssn(self, ssn: str):
		'''
		Set ssn value
		:param ssn:
		:return:
		'''
		self._ssn = ssn

	@property
	def username(self):
		'''
		Returns username value
		:return:
		'''
		return self._username

	@username.setter
	def username(self, username: str):
		'''
		Returns username value
		:param username:
		:return:
		'''
		self._username = username

	@property
	def password(self):
		'''
		Returns password value
		:return:
		'''
		return self._password

	@password.setter
	def password(self, password: str):
		'''
		Set password value
		:param password:
		:return:
		'''
		self._password = password

