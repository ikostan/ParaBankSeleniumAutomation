from page_context.base_page_context import BasePageContext


class AboutPageContext(BasePageContext):

	TITLE = BasePageContext.TITLE + 'About Us'

	URL = BasePageContext.URL + 'about.htm'

	DESCRIPTION = {'title': 'ParaSoft Demo Website',
	               'text': ['ParaBank is a demo site used for demonstration of Parasoft software solutions.',
	                        'All materials herein are used solely for simulating a realistic online banking website.',
	                        'In other words: ParaBank is not a real bank!',
	                        'For more information about Parasoft solutions please visit us at:\nwww.parasoft.com or '
	                        'call 888-305-0041']}

	LINK = "http://www.parasoft.com/"
