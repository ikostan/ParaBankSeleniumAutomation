#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from expected_results.page_content.bank_account_content import BankAccountContent


class AccountOverviewContent(BankAccountContent):

	URL = BankAccountContent.URL + 'overview.htm'
	TITLE = 'Accounts Overview'
	HEADER = 'Accounts Overview'
	ACCOUNT_CHART = {
		'columns': {'account': 'Account',
		            'balance': "Balance*",
		            'amount': "Available Amount"},
		'total': 'Total',
		'note': '*Balance includes deposits that may be subject to holds'
	}

