*** Settings ***
Resource    Resources/App.robot
Resource    Resources/Common.robot

*** Variable ***

*** Test Cases ***
Open the browser and login
    [Documetation]  Login to web application
    [Tag]  Smoke

    Common.Open the browser
    App.login to Application
    Common.close the browser

*** Keywords ***
