#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from expected_results.page_content.base_page_content import BasePageContent
from expected_results.page_content.base_personal_info_content import BasePersonalInfoContent


class ForgotLoginInfoPageContent(BasePageContent, BasePersonalInfoContent):
	'''
	Holds fields/data from "Forgot Login Info" form
	'''

	TITLE = BasePageContent.TITLE + 'Customer Lookup'

	URL = BasePageContent.URL + 'lookup.htm'

	HEADER = {
		'class': "title",
		'text': 'Customer Lookup'
	}

	DESCRIPTION = {'text': 'Please fill out the following information in order to validate your account.'}

	FIND_MY_LOGIN_INFO_BUTTON = {
		'type': "submit",
		'class': "button",
		'value': "Find My Login Info"
	}

	USERNAME = "Username: "

	PASSWORD = "Password: "

	SUCCESS_MESSAGE = 'Your login information was located successfully. You are now logged in.'

	ERROR_TITLE = 'Error!'

	ERROR_MESSAGE = 'The customer information provided could not be found.'
