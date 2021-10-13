*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***

*** Keywords ***

login to Application
    go to  https://www.saucedemo.com/
    input text  id=user-name   standard_user
    input password  id=password  secret_sauce
    click button  id=login-button

