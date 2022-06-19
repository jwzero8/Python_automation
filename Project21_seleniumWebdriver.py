from selenium import webdriver
browser = webdriver.Firefox()
type(browser) # Not a functional program, did not solve the problem, not a pragmatic programmer at this moment.
"""Damn problem solved. Reason is that module version does not match with the geckowebdriver."""

browser.get("https://inventwithpython.com")
try:
    elem = browser.find_element_by_class_name(" cover-thumb")
    print("Found <%s> element with that class name!" % (elem.tag_name))
except:
    print("Was not able to find an element with that name.")

