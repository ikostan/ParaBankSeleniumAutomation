#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from expected_results.page_content.base_page_content import BasePageContent


class AdminPageContent(BasePageContent):

	TITLE = BasePageContent.TITLE + 'Administration'

	URL = BasePageContent.URL + 'admin.htm'

	INITIALIZE_BUTTON = 'Initialize'

	CLEAN_BUTTON = 'Clean'
