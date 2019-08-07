from expected_results.page_context.base_page_context import BasePageContext


class BankAccountContext(BasePageContext):

	ACCOUNT_SERVICES_MENU = {
		'welcome_message': "Welcome ",
		'title': 'Account Services',
		"menu_items": {
			'open_new_account': {'text': 'Open New Account',
			                     "href": "/parabank/openaccount.htm"},
			'account_overview': {'text': 'Accounts Overview',
			                     "href": "/parabank/overview.htm"},
			'transfer_funds': {'text': 'Transfer Funds',
			                   "href": "/parabank/transfer.htm"},
			'bill_pay': {'text': 'Bill Pay',
			             "href": "/parabank/billpay.htm"},
			'find_transactions': {'text': 'Find Transactions',
			                      "href": "/parabank/findtrans.htm"},
			'update_info': {'text': 'Update Contact Info',
			                "href": "/parabank/updateprofile.htm"},
			'request_loan': {'text': 'Request Loan',
			                 "href": "/parabank/requestloan.htm"},
			'log_out': {'text': 'Log Out',
			            "href": "/parabank/logout.htm"}
		}
	}

