from page_context.base_page_context import BasePageContext


class AdminPageContext(BasePageContext):

	TITLE = BasePageContext.TITLE + 'Administration'

	URL = BasePageContext.URL + 'admin.htm'
