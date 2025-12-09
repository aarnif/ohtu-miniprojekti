*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations
Library   OperatingSystem

*** Test Cases ***
At start there are no citations
    Go To  ${HOME_URL}
    Title Should Be  Citations app
    Page Should Contain  No citations.

First citation can be added
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999

Second citation can be added
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613
    Add citation  book  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008  10.1145/1869452.1869473

    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Check page contains citation  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008

Citation requires Citation Type
    Go To  ${HOME_URL}
    Click Link  New citation
    Input Text  author  Martin Fowler
    Input Text  title  Refactoring: Improving the Design of Existing Code
    Input Text  publisher  Addison-Wesley
    Input Text  year  1999
    Input Text  doi  10.1145/2380552.2380613
    Click Button  Add
    Page Should Contain  Citation type is required

Citation requires Author
    Go To  ${HOME_URL}
    Click Link  New citation
    Select From List By Value  citation_type  book
    Input Text  title  Refactoring: Improving the Design of Existing Code
    Input Text  publisher  Addison-Wesley
    Input Text  year  1999
    Input Text  doi  10.1145/2380552.2380613
    Click Button  Add
    Page Should Contain  Author length must be between 3 and 100
