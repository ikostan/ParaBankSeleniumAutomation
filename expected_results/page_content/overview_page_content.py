#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from expected_results.page_content.base_page_content import BasePageContent


class OverviewPageContent(BasePageContent):

	TITLE = BasePageContent.TITLE + 'Accounts Overview'

	URL = BasePageContent.URL + 'overview.htm'

