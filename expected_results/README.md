## Expected results

<div align="center"> 
<img width="5%" height="5%" src="https://github.com/ikostan/ParaBankSeleniumAutomation/blob/master/images/iconfinder_ViewResults_46723.png" hspace="10">
</div>

When expected software testing results are not defined adequately, it is often impossible for the tester to ascertain accurately whether the actual results are right or wrong. Consider how many tests are defined in a manner similar to, "Try this function and see if it works properly." "Works properly" is a conclusion, but not a specific-enough expected result on which to base said conclusion. Yet testers often somewhat blindly take for granted that they can guess needed inputs or conditions and corresponding actual results.<br/>

For a test to be effective, we must define software testing correctness (expected software testing results) independently of actual results so the actual results do not unduly influence definition of the expected results. As a practical matter, we also need to define the expected results before obtaining the actual results, or our determination of the expected results probably will be influenced by the actual results. In addition, we need to document the expected results in a form that is not subject to subsequent conscious or unconscious manipulation.<br/>

**To describe the expected results you can refer to 3 sources (most important first):**<br/>

1. The customer’s specification: this is your bible (if you have it)! Even if you think the customer’s choice is weird (your opinion), don’t describe a different expected behaviour than the one presented in the customer’s specification. If you disagree with the customer, write a suggestion instead and explain why you think it is more user-friendly.<br/>
2. Web standards: refer to the web standards when you don’t have the customer’s specification. Web standards means “widely spread behaviour across websites”. For example, the navigation bar is commonly at the top or on the left side. A search bar is commonly a text field with a placeholder and a magnifying glass icon at the right border. In a list, the entries are generally sorted by alphabetical order. These are not unchanging rules. They are just commonly known behaviours. Over time, they have become a user-friendly behaviours.<br/>
3. Your own analysis: at last, sometimes describing the expected behaviour equals to writing the common sense. For example, you have just set a filter, you would expect it to change the related list. In these cases, you don’t need a specification to write what was the expected result.<br/>

Source:<br>
[Chapter 2: How to write useful “Actual and Expected results” details in your bug report](https://medium.com/we-are-testers/chapter-2-how-to-write-useful-actual-and-expected-results-details-in-your-bug-report-10b83e5aaa75)<br/>
[Define expected software testing results independently](https://searchsoftwarequality.techtarget.com/photostory/4500248704/Four-tips-for-effective-software-testing/2/Define-expected-software-testing-results-independently)

