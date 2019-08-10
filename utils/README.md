# Utils

Contains a collection of various functions.

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

<br/>Is a solution using a decorator that wrapps every method on a class that starts test_ with a wrapper that takes a screenshot if the method raises and Exception. The browser_attr is used to tell the decorator how to obtain the web browser (driver).

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
  <summary><b></b></summary>

<br/><br/>

</details>

### browser_configuration() function:
   Simplifies cross browser testing. By default it returns 'chrome' value. Every Test class has it by default as part of setUpClass definition. See example bellow:
  
```python
@classmethod
    def setUpClass(cls):
        with allure.step("Open web browser"):
            cls.browser = browser_configuration()
            cls.page_model = AboutPageModel
            cls.page_context = AboutPageContext
            cls.page = open_web_browser(browser=cls.browser, page_model=cls.page_model, page_context=cls.page_context)
```

<details>
  <summary><b></b></summary>

<br/><br/>

</details>
