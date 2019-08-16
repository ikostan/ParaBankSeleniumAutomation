## Utils

<div align="right"> 
<img width="7%" height="7%" src="https://github.com/ikostan/ParaBankSeleniumAutomation/blob/master/images/utils.png" hspace="10">
</div>

Contains a collection of various help classes and functions, see list bellow:

<details>
  <summary><b>Driver Class</b></summary>

<br/>In order to instantiate webdriver I use Driver class of my own. The main idea behind it is to simplify working process with Selenium 'webdriver' object.
In order to create webdriver object you just do the following:<br/> 

```python
    from utils.driver import Driver
    
    # Chrome:
    driver = Driver('chrome', is_debug=True)
    
    # FireFox:
    driver = Driver('mozilla', is_debug=True)
    
    # Edge:
    driver = Driver('edge', is_debug=True)
```

<br/>**Supported browsers:**<br/> 
    - Chrome<br/> 
    - Firefox<br/> 
    - Edge<br/> 
</details>

<details>
  <summary><b>step_definition function</b></summary>

<br/>

**"Arrange-Act-Assert"** a pattern for arranging and formatting code in UnitTest methods.<br/>
The function is grouping following functional sections:<br/>

1. Arrange all necessary preconditions and inputs.
2. Act on the object or method under test.
3. Assert that the expected results have occurred.

**Benefits:**<br/>
1. Clearly separates what is being tested from the setup and verification steps.<br/>
2. Clarifies and focuses attention on a historically successful and generally necessary set of test steps.<br/>
3. Makes some TestSmells more obvious:<br/>
    - Assertions intermixed with "Act" code.<br/>
    - Test methods that try to test too many different things at once.<br/>

Source:<br/>
- [Unit Testing and the Arrange, Act and Assert (AAA) Pattern](https://medium.com/@pjbgf/title-testing-code-ocd-and-the-aaa-pattern-df453975ab80)<br/>
- [Arrange Act Assert](http://wiki.c2.com/?ArrangeActAssert)<br/>
<br/>

</details>

<details>
  <summary><b>screenshot_on_fail wrapper</b></summary>

<br/>Is a solution using a decorator that wrapps every method on a class that starts test_ with a wrapper that takes a screenshot if the method raises and Exception. 

   ```python
    from utils.screenshot import screenshot_on_fail

    @screenshot_on_fail()
    class HomePageTestCase(BaseTestCase):
    
        def test_context_base_elements_chrome(self):
    
            # Open web page
            browser = 'chrome'
            driver = Driver(browser)
            self.page = HomePageModel(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
            self.page.go()
    
            # Test base context:
            self.assertEqual(HomePageContext.URL,
                             self.page.url)
```
                             
Source: https://stackoverflow.com/questions/12024848/automatic-screenshots-when-test-fail-by-selenium-webdriver-in-python
<br/>
</details>


<details>
  <summary><b>clean_database() method</b></summary>

<br/>

- Clean and initialise database<br/>
- Does not check for any errors<br/>
- Using open_web_browser method in order to instantiate Selenium webdriver<br/>
- Provides following log (print function): 'Cleaning database...', 'Initializing database...'<br/>
- See example below:<br/><br/>
    
```python
    class TestUserRegistration(UserRegistrationCase):

	@classmethod
	def setUpClass(cls):
		cls.client = JaneDoe
		cls.browser = 'chrome'
		cls.page = None

		with allure.step("Initial data setup > clean DB"):
			clean_database()
```

</details>


<details>
  <summary><b>get_http_status_code(url) method</b></summary>

<br/>

- Returns HTTP status code<br/>
- Using requests library<br/>
- See sample output bellow:<br/>
<br/>	

```
    URL: https://parabank.parasoft.com/parabank/about.htm
    HTTP Status code: 200
```
	
<br/>
</details>


<details>
  <summary><b>open_web_browser(browser: str, page_model, page_context) method</b></summary>

<br/>

   **Takes care of following procedure:**<br/>
       
   1. Instantiate Selenium webdriver<br/>
   2. Instantiate Page Model Object<br/>
   3. Checks HTTP status code<br/>
   4. Open web browser > open test web page<br/>
   5. Refresh web browser in case test web site is not loaded<br/>
   6. Returns page instance (Page Model Object)<br/>
		
   <br/>See example below:<br/><br/>

```python
    class TestAboutPageContext(AboutPageContextCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = browser_configuration()
			cls.page_model = AboutPageModel
			cls.page_context = AboutPageContext
			cls.page = open_web_browser(browser=cls.browser,
			                            page_model=cls.page_model,
			                            page_context=cls.page_context)
```
	
<br/>
</details>


<details>
  <summary><b>DriverPath class</b></summary>

<br/>

- Contains local path for Selenium webdriver<br/>
- Used in case system has no PATH configuration<br/>
<br/>
</details>

</details>


<details>
  <summary><b>refresh_page(expected, page, sleep_time=3) method</b></summary>

<br/>
    1. Check if page has expected title<br/>
	2. Trying to refresh web page in case page title dos not equal expected result<br/>
	3. Raises exception in case page title dos not equal expected result<br/>
<br/>
</details>


<details>
  <summary><b>register_user(client) method</b></summary>

<br/>

- Registers a new user.
- Does not check for any errors.
- Using Selenium webdriver + chrome browser by default
<br/>

</details>
