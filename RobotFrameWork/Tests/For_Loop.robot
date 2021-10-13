*** Settings ***
Library  Seliniumlibrary

*** Test Cases ***
ForLoop
    :FOR   ${i}     IN   RANG  1    10
      \  Log to console  ${i}

      :FOR   ${i}     IN   1    2   3   4   5   6   7
            \  Log to console  ${i}

       @{iteam}     create list     1   4   7   97  61
      :FOR   ${i}     IN   @{iteam}
      \  Log to console  ${i}

*** Keywords ***
Provided precondition
    Setup system under test