*** Settings ***
Documentation    Suite description

*** Test Cases ***
Test title
    open browser

    #Right click
    open context menu  xpath:

    #Double click
    double click element  id:

    # Drag and drop
    drag and drop  id:resource  id:Target

*** Keywords ***
Provided precondition
    Setup system under test