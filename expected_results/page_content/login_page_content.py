#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from expected_results.page_content.base_page_content import BasePageContent


class LoginPageContent(BasePageContent):

	TITLE_ERROR = BasePageContent.TITLE + 'Error'

	URL = BasePageContent.URL + 'login.htm'

	ERROR_TITLE = 'Error!'
	ERROR_MESSAGE = 'The username and password could not be verified.'


