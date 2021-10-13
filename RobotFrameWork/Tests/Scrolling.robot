*** Settings ***
Library  SeleniumLibrary

*** Variable ***
${browser}  gc
${url}  http://demowebshop.tricentis.com/

*** Test Cases ***
Speed test
    open browser  ${url}  ${browser}
    maximize browser window

    #scrolling down by pixel
    #execute javascript  window.scrollTo(0,400)

    #scrolling down till element
    #scroll element into view  xpath:/html/body/div[4]/div[1]/div[4]/div[3]/div/div/div[3]/div[5]/div/div[2]/h2/a

    #till end
    execute javascript  window.scrollTo(0,document.body.scrollHeight)
    sleep  2s
    execute javascript  window.scrollTo(0,-document.body.scrollHeight)
*** Keywords ***
Provided precondition
    Setup system under test