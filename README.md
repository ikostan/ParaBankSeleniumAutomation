[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
# Selenium Automation for Para Bank Web App

<div align="center"> 
<img width="50%" height="50%" src="https://github.com/ikostan/ParaBankSeleniumAutomation/blob/master/images/selenium-python-logo.png" hspace="10">
</div>

### ParaSoft Demo Website<br/>
ParaBank is a demo site used for demonstration of Parasoft software solutions. 
All materials herein are used solely for simulating a realistic online banking website.

In other words: ParaBank is not a real bank!

[Demo Website](https://parabank.parasoft.com/parabank/index.htm)<br/>
[Read more about Para Bank demo website available services](https://parabank.parasoft.com/parabank/services.htm)<br/>

### Official Documentation:<br/>

**[Selenium Documentation](https://seleniumhq.github.io/selenium/docs/api/py/api.html)**<br/>

**[Full pytest documentation](http://doc.pytest.org/en/latest/contents.html)**<br/>

**['Selenium with Python' official documentation webpage](https://selenium-python.readthedocs.io)**<br/>

### Dev Environment:<br/>
1. Python 3.7<br/>
2. selenium 3.141.0<br/>
3. PyCharm 2019.1.3 (Community Edition)<br/>
4. Win 10 (64 bit)<br/>

[PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html)<br/>

### Supported/tested browsers:
- Chrome: v75 (64 bit)
- Firefox: v68 (64  bit)
- Edge: v17 and above

**PyCharm - Choosing Your Testing Framework:**<br/>

1. Open the Settings/Preferences dialog, and under the node Tools, click the page Python Integrated Tools.<br/>
2. On this page, click the Default Test Runner field.<br/>
3. Choose the desired test runner:<br/>

For more info please see [Enable Pytest for you project](https://www.jetbrains.com/help/pycharm/pytest.html)

<br/>   
<div align="center"> 
<img width="100%" height="100%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/py_choosing_test_runner.png" hspace="20">
</div>
<br/>

<br/>**Setting up Python3 virtual environment on Windows machine:**<br/>

1. open CMD
2. navigate to project directory, for example:<br/> 
```bash
cd C:\Users\superadmin\Desktop\Python\CodinGame
```
3. run following command:<br/> 
```bash 
pip install virtualenv
```
4. run following command:<br/> 
```bash 
virtualenv venv --python=python
```

<br/>**Changing the project interpreter in the PyCharm project settings:**<br/>
1. In the **Settings/Preferences dialog** (Ctrl+Alt+S), select **Project <project name> | Project Interpreter**.<br/>
2. Expand the list of the available interpreters and click the **Show All** link.<br/>
3. Select the target interpreter. When PyCharm stops supporting any of the outdated Python versions, the corresponding project interpreter is marked as unsupported.<br/>
4. The Python interpreter name specified in the **Name** field, becomes visible in the list of available interpreters. Click **OK** to apply the changes.<br/>

For more info please check [here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)<br/>

### Tech Issues and Problem Solving:<br/>

- **How to fix in case .gitignore is ignored by Git:**<br/>

Even if you haven't tracked the files so far, Git seems to be able to "know" about them even after you add them to .gitignore.<br/> 

    **NOTE:**<br/>
    - First commit your current changes, or you will lose them.<br/> 
    - Then run the following commands from the top folder of your Git repository:<br/> 
    ```bash 
    git rm -r --cached .
    git add .
    git commit -m "fixed untracked files"
    ```

- **[How to fix common Selenium errors?](https://www.ultimateqa.com/common-selenium-webdriver-errors-fix/)**<br/>

- **Microsoft webdriver for edge 18 and above:**<br/>
    MS made WebDriver a Windows Feature on Demand (FoD), which ensures that it’s always up to date automatically, and enables some new ways to get Microsoft WebDriver.<br/>
    
    The simplest way to get started is simply to enable Developer Mode. Simply open the Settings app and go to “Update & Security,” “For developers,” and select “Developer Mode.” The appropriate version of WebDriver will be automatically installed.<br/>
    
    You can also install a standalone version of WebDriver in one of two ways:<br/>
    * Search “Manage optional features” from Start, then select “Add a Feature,” “WebDriver.”<br/>
    * Install via DISM by running the following command in an elevated command prompt:
    <br/>```DISM.exe /Online /Add-Capability /CapabilityName:Microsoft.WebDriver~~~~0.0.1.0```<br/>
    
    This also means that we will no longer be providing standalone downloads for Microsoft WebDriver going forward<br/>
    
    Source: https://blogs.windows.com/msedgedev/2018/06/14/webdriver-w3c-recommendation-feature-on-demand/#Rg8g2hRfjBQQVRXy.97
    
- **selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Opera binary**

    ```python
    from selenium.webdriver.opera.options import Options
    
    options = Options()
    options.binary_location = r'<path to opera.exe>' 
    opera_web_driver_path = r'<path to operadriver.exe>' 
    driver = webdriver.Opera(options=options, executable_path=opera_web_driver_path)
    driver.get(<url>)
    driver.close()
    ```
    Source: https://stackoverflow.com/questions/52793537/selenium-common-exceptions-webdriverexception-message-unknown-error-cannot-fi

- **Internet Explorer browser window not getting closed in Selenium Webdriver**

    ```bash
    1. Open IE browser
    2. Go to Internet Options >>> Security
    3. For every zone heck "Enable Protected Mode"
    4. Restart IE
    ```

- **Test are failed due to slow performance of WebDriver**<br/>
    Explicit wait is used to specify wait condition for a particular element.<br/> 
    Here we define to wait for a certain condition to occur before proceeding further in the code.
    ```python
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    
    # Wait for element to appear:
    wait = WebDriverWait(self.driver, 10)
    wait.until(ec.title_is(self.new_window_name))
    ```

- **How to Get Selenium to Wait for Page Load After a Click:**<br/>
    It turns out Selenium has a built-in condition called staleness_of, as well as its own wait-for implementation. 
    Use them, alongside the @contextmanager decorator and the magical-but-slightly-scary yield keyword, and you get:

    ```python
    from contextlib import contextmanager
    from selenium.webdriver.support.ui import WebDriverWait 
    from selenium.webdriver.support.expected_conditions import staleness_of
    
    class MySeleniumTest(SomeFunctionalTestClass): 
      # assumes self.browser is a selenium webdriver
    
      @contextmanager
      def wait_for_page_load(self, timeout=30):
        old_page = self.browser.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.browser, timeout).until(
          staleness_of(old_page)
        )
        
      def test_stuff(self):
        # example use
        with self.wait_for_page_load(timeout=10):
          self.browser.find_element_by_link_text('a link')
    ```
    
    **Note** that this solution only works for “non-JavaScript” clicks, i.e., clicks that will cause the browser to load a brand new page, and thus load a brand new HTML body element.
    <br/>Source: https://blog.codeship.com/get-selenium-to-wait-for-page-load/

- **[Required Configuration - IE only](https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver):**<br/>
    
    1. The IEDriverServer exectuable must be downloaded and placed in your **PATH**.<br/>
    2. On IE 7 or higher on Windows Vista or Windows 7, you must set the **Protected Mode** settings for each zone to be the same value. The value can be on or off, as long as it is the same for every zone. To set the Protected Mode settings, choose "Internet Options..." from the Tools menu, and click on the Security tab. For each zone, there will be a check box at the bottom of the tab labeled "Enable Protected Mode".<br/>
    3. Additionally, **"Enhanced Protected Mode"** must be disabled for IE 10 and higher. This option is found in the Advanced tab of the Internet Options dialog.<br/>
    4. The browser zoom level must be set to 100% so that the native mouse events can be set to the correct coordinates.<br/>
    5. For Windows 10, you also need to set *"Change the size of text, apps, and other items"* to 100% in display settings.<br/>
    6. For IE 11 only, you will need to set a registry entry on the target computer so that the driver can maintain a connection to the instance of Internet Explorer it creates. For 32-bit Windows installations, the key you must examine in the registry editor is *HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE*. For 64-bit Windows installations, the key is *HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE*. Please note that the *FEATURE_BFCACHE* subkey may or may not be present, and should be created if it is not present. Important: Inside this key, create a *DWORD* value named *iexplore.exe* with the value of *0*.<br/>

- **NoSuchWindowException in IE 11:**<br/>

    1. IE Options --> Security Tab -> Uncheck "Enable Protected Mode".
    2. Add http://localhost/ to your trusted sites in IE11. 
    3. Registry keys:
    <br/>For 64-bit Windows installations, the key is:<br/> 
    ``` HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet explorer\Main\FeatureControl\FEATURE_BFCACHE```
    <br/>For 32-bit Windows installations, the key is:<br/> 
    ```HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE```
     
    <br/>Source: https://stackoverflow.com/questions/24746777/selenium-nosuchwindowexception-in-ie-11