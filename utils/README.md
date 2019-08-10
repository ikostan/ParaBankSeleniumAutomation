# Utils

Contains a collection of various help classes and functions, see list bellow:

<details>
  <summary><b>Driver Class</b></summary>

<br/>The main idea behind it is to simplify working process with Selenium 'webdriver' object.
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

<br/>**Supported browsers:**
    - Chrome<br/> 
    - Firefox<br/> 
    - Edge<br/> 
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
  <summary><b>browser_configuration() function</b></summary>

<br/>
   - Simplifies cross browser testing.<br/>
   - Returns browser name from from predefined dictionary.<br/>
   - By default it returns 'chrome' value.<br/>
   - Provides following log (simple type function): 'Run configuration: chrome'
   - Every Test class has it by default as part of setUpClass definition. See example bellow:<br/>
  
```python
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
  <summary><b>clean_database() method</b></summary>

<br/>
    - Clean and initialise database<br/>
	- Does not check for any errors<br/>
    - Using open_web_browser method in order to instantiate Selenium webdriver<br/>
    - Provides following log (print function): Cleaning database...<br/>
                                               Initializing database...<br/>
    - See example below:<br/>
    
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
    - Returns HTTP status code
	- Using requests library
	- See sample output bellow:
	
```python
    URL: https://parabank.parasoft.com/parabank/about.htm
    HTTP Status code: 200
```
	
<br/>
</details>


<details>
  <summary><b></b></summary>

<br/>
    
<br/>
</details>


<details>
  <summary><b></b></summary>

<br/>
    
<br/>
</details>

</details>


<details>
  <summary><b></b></summary>

<br/>
    
<br/>
</details>

