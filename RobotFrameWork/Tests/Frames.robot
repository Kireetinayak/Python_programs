*** Settings ***
Library    SeleniumLibrary

*** Variable ***
${Browser}  gc
${URL}  https://demo.nopcommerce.com/
*** Test Cases ***
Test Frames
    oprn browser  ${url} ${Browser}
    #select frames
    select frame  # name , id, xpath
    click element  id: get keyword names
    unselect frame # name , id, xpath




*** Keywords ***
Provided precondition
    Setup system under test