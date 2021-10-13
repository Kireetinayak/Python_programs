*** Settings ***
Library  SeleniumLibrary

*** Variable ***
${browser}  gc
${url}  http://demowebshop.tricentis.com/

*** Test Cases ***
Speed test
    open browser  ${url}  ${browser}
    maximize browser window
    #sleep
   # sleep 5s # defalut it will stop the script for 5s

    #selenium sleep
   # set selenium speed  3s  # Every step wit will wait for 3s

    #selenium  timeout
   #selenium set timeout  10s
   #wait until page contains  Registration  #5s default

   #Implicit wait
    set selenium implicit wait  10s
    click link  xpath:/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a
    select radio button  Gender  M
    input text  id:FirstName  King
    input text  id:LastName  Nayak
    input text  id:Email  king@gmail.com
    click button  id:register-button

*** Keywords ***
