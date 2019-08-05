from expected_results.page_context.base_page_context import BasePageContext
from expected_results.page_context.base_personal_info import BasePersonalInfo


class ForgotLoginInfoPageContext(BasePageContext, BasePersonalInfo):
	'''
	Holds fields/data from "Forgot Login Info" form
	'''

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
