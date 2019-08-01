from page_context.base_page_context import BasePageContext


class HomePageContext(BasePageContext):
	'''
	Holds expected context values for home page items
	'''

	URL = BasePageContext.URL + 'index.htm'

	TITLE = BasePageContext.TITLE + 'Welcome | Online Banking'

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
		'title': 'Online Services',
		'Bill Pay': {'text': 'Bill Pay',
		             'href': "services/bank?_wadl&_type=xml"},
		'Account History': {'text': 'Account History',
		                    'href': "services/bank?_wadl&_type=xml"},
		'Transfer Funds': {'text': 'Transfer Funds',
		                   'href': "services/bank?_wadl&_type=xml"}
	}

	READ_MORE_SERVICES = {'href': "services.htm",
	                      'text': 'Read More'}

	LATEST_NEWS = 'Latest News'

	READ_MORE_NEWS = {'text': 'Read More',
	                  "href": "news.htm"}

