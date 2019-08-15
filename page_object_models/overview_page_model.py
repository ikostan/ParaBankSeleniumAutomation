#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from page_object_models.base_page_model import BasePageModel
from expected_results.page_content.overview_page_content import OverviewPageContent


class OverviewPageModel(BasePageModel):
	"""
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	"""

	_url = OverviewPageContent.URL


