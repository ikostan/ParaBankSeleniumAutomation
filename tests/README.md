## Tests Folder

<div align="right"> 
<img width="7%" height="7%" src="https://github.com/ikostan/ParaBankSeleniumAutomation/blob/master/images/iconfinder_stock_task_24333.png" hspace="10">
</div>

Contains ParaBank online banking automated tests.<br/>

### Table of Contents:<br/>
1. <a href="#guidelines">General Guidelines</a>
2. <a href="#config">Environment Configuration</a>
3. [Content Tests](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/content_tests)<br/>
   - [Base Cases](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/content_tests/base_cases)<br/>
   - [Base Content Tests](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/content_tests/base_content_tests)<br/>
   - [Unique Content Tests](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/content_tests/base_content_tests)<br/>
4. [End To End Tests](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/e2e_tests)<br/>
   - [Log In / Log Out](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/e2e_tests/login_logout)<br/>
   - [User Registration](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/tests/e2e_tests/user_registration)<br/>

### <a id="guidelines"></a>General Guidelines:<br/>

The general guidelines for the tests are based on following resources:<br/>

- [How To Test Banking Domain Applications: A Complete BFSI Testing Guide](https://www.softwaretestinghelp.com/testing-banking-applications/)
- [How To Test Retail Banking System](https://www.softwaretestinghelp.com/how-to-test-retail-banking-system/)
- [Agile process work item types and workflow](https://docs.microsoft.com/en-us/azure/devops/boards/work-items/guidance/agile-process-workflow?view=azure-devops)

<div align="center"> 
<img width="100%" height="100%" src="https://github.com/ikostan/ParaBankSeleniumAutomation/blob/master/images/agile-process-plan-wits.png" hspace="10">
</div>

<details>
  <summary><b><a id="config"></a>Environment Configuration: Config class</b></summary>

<br/>

[Config Class](https://github.com/ikostan/ParaBankSeleniumAutomation/blob/master/tests/config.py):<br/>

- Simplifies cross browser testing.<br/>
- Returns browser name from from predefined dictionary.<br/>
- By default it returns 'chrome' value.<br/>
- Provides following log (simple type function): 'Run configuration: chrome....'<br/>
- Every Test class has it by default as part of setUpClass definition.<br/>
- See example bellow:<br/>
<br/>
 
```python
class TestHomeBasePageContent(BaseContentCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.app_config = Config()
			cls.page_model = HomePageModel
			cls.page_content = HomePageContent
			cls.page = open_web_browser(browser=cls.app_config.browser,
			                            page_model=cls.page_model,
			                            page_content=cls.page_content)
```
<br/>
</details>