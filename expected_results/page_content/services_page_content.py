#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


from expected_results.page_content.base_page_content import BasePageContent


class ServicesPageContent(BasePageContent):

	TITLE = BasePageContent.TITLE + 'Services'

	URL = BasePageContent.URL + 'services.htm'
