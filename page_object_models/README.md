## Page Object Model (POM)

### Introduction<br/>

Page Object Model is a design pattern to create Object Repository for web UI elements. Under this model, for each web page in the application, there should be corresponding page class. This Page class will find the WebElements of that web page and also contains Page methods which perform operations on those WebElements.<br/>

### Problem<br/>

When you are writing functional tests using Selenium a major part of your code will consist of interactions with the web interface you are testing through the WebDriver API. After fetching elements you will verify some state of the element through various assertions and move on to fetching the next element.<br/>

Even with a simple test readability is very poor. There is a lot of WebDriver code, that obscures the purpose of the test, making it slow and difficult to digest.<br/>

With any interface, and I suppose web interfaces in particular, it is common that both minor and major changes to the UI is implemented frequently. This could be a new design, restructuring of fields and buttons, and this will likely impact your test. So your test fails and you need to update your selectors.<br/>

Some of the typical problems for this type of Selenium test are:<br/>

- Test cases are difficult to read<br/>
- Changes in the UI breaks multiple tests often in several places<br/>
- Duplication of selectors both inside and across tests - no reuse<br/>

### Solution<br/>

So instead of having each test fetch elements directly and being fragile towards UI changes, the Page Object Pattern introduces what is basically a decoupling layer.<br/>

You create an object that represents the UI you want to test, which could be a whole page or a significant part of it. The responsibility of this object is to wrap HTML elements and encapsulate interactions with the UI, meaning that this is where all calls to WebDriver will go. This is where most WebElements are. And this is the only place you need to modify when the UI changes.<br/>

This figure illustrates the pattern:<br/>

<br/>   
<div align="center"> 
<img width="60%" height="60%" src="https://github.com/ikostan/ParaBankSeleniumAutomation/blob/master/images/pom_pattern.png" hspace="20">
</div>
<br/>

### Advantages of POM<br/>

1. Page Object Pattern says operations and flows in the UI should be separated from verification. This concept makes our code cleaner and easy to understand.<br/>
2. The Second benefit is the object repository is independent of test cases, so we can use the same object repository for a different purpose with different tools. For example, we can integrate POM with TestNG/JUnit for functional Testing and at the same time with JBehave/Cucumber for acceptance testing.<br/>
3. Code becomes less and optimized because of the reusable page methods in the POM classes.<br/>
4. Methods get more realistic names which can be easily mapped with the operation happening in UI. i.e. if after clicking on the button we land on the home page, the method name will be like 'gotoHomePage()'.<br/>
5. Any change in UI can easily be implemented, updated and maintained into the Page Objects and Classes.


### Best practices<br/>

There are a few best practices in using page objects, that you should make an effort to follow.<br/>

- A page object should not have any assertions<br/>
- A page object should represent meaningful elements of a page and not necessarily a complete page<br/>
- When you navigate you should return the a page object for the next page<br/>


### Implementation involves following steps<br/>

1. Review the overall flow of UI Screens.<br/>
2. All page models can inherit from the Page super class.<br/>
3. Create a Page class for every UI screen.<br/>
4. A Page Class should return another Page class (via an operation) which represents the next screen in a flow.<br/>
5. Create Test classes and test methods which perform operations on Page Objects.<br/>


**Sources:**<br/>
- [Page Object Model (POM) & Page Factory: Selenium WebDriver Tutorial](https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html)<br/>
- [Page Object Model (POM) | Design Pattern](https://medium.com/tech-tajawal/page-object-model-pom-design-pattern-f9588630800b)<br/>
- [Getting Started with Page Object Pattern for Your Selenium Tests](https://www.pluralsight.com/guides/getting-started-with-page-object-pattern-for-your-selenium-tests)<br/>
- [Design Patterns - Page Object Model](https://docs.experitest.com/display/TE/Design+Patterns+-+Page+Object+Model)<br/>
- [Page Object Model (Selenium, Python)](https://qxf2.com/blog/page-object-model-selenium-python/)
