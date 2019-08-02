from page_models.base_page_model import BasePageModel
from page_context.services_page_context import ServicesPageContext


class ServicesPageModel(BasePageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	_url = ServicesPageContext.URL


