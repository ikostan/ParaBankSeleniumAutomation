# Utils

### Driver package:<br/> 

The main idea behind it is to simplify working process with Selenium 'webdriver' object.
In order to create webdriver object you just do the following:<br/> 
```python
from utils.driver import Driver
driver = Driver('chrome').get_driver()
```

**Supported browsers:**
- Chrome<br/> 
- Firefox<br/> 
- Edge<br/> 
