def register_user(page, client):
	'''
	Register a new user.
	Does not check for any errors.
	:param page:
	:param client:
	:return:
	'''

	page.type_first_name(client.FIRST_NAME)

	page.type_last_name(client.LAST_NAME)

	page.type_address(client.ADDRESS)

	page.type_city(client.CITY)

	page.type_state(client.STATE)

	page.type_zip_code(client.ZIP_CODE)

	page.type_phone(client.PHONE)

	page.type_ssn(client.SSN)

	page.type_username(client.USERNAME)

	page.type_password(client.PASSWORD)

	page.type_confirm(client.PASSWORD)

	page.click_register_btn()
