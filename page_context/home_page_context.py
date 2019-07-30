from page_context.base_page_context import BasePageContext


class HomePageContext(BasePageContext):
	'''
	Holds expected context values for home page items
	'''

	URL = BasePageContext.ROOT_URL + '/index.htm'

	TITLE = 'ParaBank | Welcome | Online Banking'

	ATM_SERVICES = {
		'title': 'ATM Services',
		'Withdraw Funds': {'text': 'Withdraw Funds',
		                   'href': "services/ParaBank?wsdl"},
		'Transfer Funds': {'text': 'Transfer Funds',
		                   'href': "services/ParaBank?wsdl"},
		'Check Balances': {'text': 'Check Balances',
		                   'href': "services/ParaBank?wsdl"},
		'Make Deposits': {'text': 'Make Deposits',
		                  'href': "services/ParaBank?wsdl"}
	}

	ONLINE_SERVICES = {
		
	}

