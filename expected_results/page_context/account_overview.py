from expected_results.page_context.bank_account_context import BankAccountContext


class AccountOverviewContext(BankAccountContext):

	URL = BankAccountContext.URL + 'overview.htm'
	TITLE = 'Accounts Overview'
	HEADER = 'Accounts Overview'
	ACCOUNT_CHART = {
		'columns': {'account': 'Account',
		            'balance': "Balance*",
		            'amount': "Available Amount"},
		'total': 'Total',
		'note': '*Balance includes deposits that may be subject to holds'
	}

