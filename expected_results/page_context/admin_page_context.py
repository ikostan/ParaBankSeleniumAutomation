from expected_results.page_context.base_page_context import BasePageContext


class AdminPageContext(BasePageContext):

	TITLE = BasePageContext.TITLE + 'Administration'

	URL = BasePageContext.URL + 'admin.htm'

	INITIALIZE_BUTTON = 'Initialize'

	CLEAN_BUTTON = 'Clean'
