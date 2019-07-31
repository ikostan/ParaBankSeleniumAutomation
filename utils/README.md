# Utils

### Driver Class:<br/> 

The main idea behind it is to simplify working process with Selenium 'webdriver' object.
In order to create webdriver object you just do the following:<br/> 
```python
from utils.driver import Driver

# Chrome:
driver = Driver('chrome').get_driver()

# FireFox:
driver = Driver('mozilla').get_driver()

# Edge:
driver = Driver('edge').get_driver()
```

**Supported browsers:**
- Chrome<br/> 
- Firefox<br/> 
- Edge<br/> 

### screenshot_on_fail wrapper:
   Is a solution using a decorator that wrapps every method on a class that starts test_ with a wrapper that takes a screenshot if the method raises and Exception. The browser_attr is used to tell the decorator how to obtain the web browser (driver).

```
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
