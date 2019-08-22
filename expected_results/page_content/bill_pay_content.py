#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from expected_results.page_content.base_page_content import BasePageContent


class BillPayContent(BasePageContent):

	URL = BasePageContent.URL + 'billpay.htm'
	HEADER = 'Bill Payment Service'
	DESCRIPTION = 'Enter payee information'

	BILL_PAYMENT_COMPLETE_TITLE = 'Bill Payment Complete'
	PAYMENT_MESSAGE = 'Bill Payment to <full_name> ' \
	                  'in the amount of $<total_amount>' \
	                  'from account <account_number> was successful.'
	MORE_DETAILS_MESSAGE = 'See Account Activity for more details.'

	FORM = {
		'payee name': {
			'title': 'Payee Name:',
			'input': {
				'name': "payee.name",
				'class': 'input',
				'type': 'text'
			},
			'error': 'Payee name is required.',
		},
		'address': {
			'title': 'Address:',
			'input': {
				'name': "payee.address.street",
				'class': 'input',
				'type': 'text'
			},
			'error': 'Address is required.'
		},
		'city': {
			'title': 'City:',
			'input': {
				'name': "payee.address.city",
				'class': 'input',
				'type': 'text'
			},
			'error': 'City is required.'
		},
		'state': {
			'title': 'State:',
			'input': {
				'name': "payee.address.state",
				'class': 'input',
				'type': 'text'
			},
			'error': 'State is required.'
		},
		'zip code': {
			'title': 'Zip Code:',
			'input': {
				'name': "payee.address.zipCode",
				'class': 'input',
				'type': 'text'
			},
			'error': 'Zip Code is required.'
		},
		'phone': {
			'title': 'Phone #:',
			'input': {
				'name': "payee.phoneNumber",
				'class': 'input',
				'type': 'text'
			}
		},
		'account': {
			'title': 'Account #:',
			'input': {
				"class": "input ng-pristine ng-valid ng-empty ng-touched",
				"name": "payee.accountNumber"
			},
			'error': "Account number is required."
		},
		'verify account': {
			'title': 'Verify Account #:',
			'input': {
				"class": "input ng-pristine ng-untouched ng-valid ng-empty",
				"name": "verifyAccount"
			},
			'error': "Account number is required."
		},
		'amount': {
			'title': "Amount: $",
			"input": {
				"class": "input ng-pristine ng-untouched ng-valid ng-empty",
				"name": "amount"
			},
			'error': "The amount cannot be empty."
		},
		"from account": {
			'title': "From account #:",
			'select': {
				"name": "fromAccountId",
				"class": "input ng-pristine ng-untouched ng-valid ng-not-empty"
			}
		}
	}

	SEND_PAYMENT_BUTTON = {
		"input": {
			"type": "submit",
			"class": "button",
			"value": "Send Payment"
		}
	}

