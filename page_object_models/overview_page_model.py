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

	def hit_log_out_button(self):
		'''
		1. Click on "Log Out"
		2. Wait until URL changes
		3. Returns HomePageModel object on success
		:return:
		'''

		super().hit_log_out_button()
		from page_object_models.home_page_model import HomePageModel
		return HomePageModel(self.driver,
		                     implicit_wait_time=5,
		                     explicit_wait_time=10)


