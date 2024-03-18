# Autotest-for-different-interface-languages
We want the online shop we are developing to work equally well for users from any country. To make sure that the solution with support for different languages works, we plan to run a set of autotests for each language. As an autotest developer, you need to implement a solution that will allow you to run autotests for different user languages by passing the required language in the command line.

1. Create a GitHub repository with the conftest.py and test_items.py files.
2. Add a handler to the conftest.py file that reads the language parameter from the command line.
3. Implement the logic in conftest.py to run a browser with the specified user language. The browser should be declared in the browser fixture and passed to the test as a parameter.
4. In the file test_items.py write a test that checks that the product page on the site contains a button to add to cart. For example, you can test a product available at http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
5. The test should be run with the language parameter with the following command:
pytest --language=es test_items.py
and pass successfully. It is enough that the code works only for the Chrome browser.
