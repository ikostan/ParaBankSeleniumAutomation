#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from expected_results.page_content.base_page_content import BasePageContent


class AboutPageContent(BasePageContent):

	TITLE = BasePageContent.TITLE + 'About Us'

	URL = BasePageContent.URL + 'about.htm'

	DESCRIPTION = {'title': 'ParaSoft Demo Website',
	               'text': ['ParaBank is a demo site used for demonstration of Parasoft software solutions.\n'
	                        'All materials herein are used solely for simulating a realistic online banking website.',
	                        'In other words: ParaBank is not a real bank!',
	                        'For more information about Parasoft solutions please visit us at:\nwww.parasoft.com or '
	                        'call 888-305-0041']}

	LINK = "http://www.parasoft.com/"
