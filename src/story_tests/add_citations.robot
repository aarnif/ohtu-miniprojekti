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
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  refactoring  design

Second citation can be added
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613  refactoring  design
    Add citation  book  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008  10.1145/1869452.1869473  practices  clean-code
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  refactoring  design
    Check page contains citation  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008  practices  clean-code

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

Citation can be added with doi link
    Go To  ${HOME_URL}
    Click Link  New citation
    Input Text  doi-fetch  https://doi.org/10.1145/2380552.2380613
    Execute JavaScript  document.getElementById('doi-fetch').blur()
    Wait Until Page Contains  ✓ Citation loaded from DOI!
    Sleep  1s
    ${selected}=  Get Selected List Value  citation_type
    Should Be Equal  ${selected}  proceedings
    Textfield Value Should Be  author  Matti Luukkainen, Arto Vihavainen, Thomas Vikberg
    Textfield Value Should Be  title  Three years of design-based research to reform a software engineering curriculum
    Textfield Value Should Be  publisher  ACM
    Textfield Value Should Be  year  2012
    Textfield Value Should Be  doi  10.1145/2380552.2380613
    Input Text  new-tag  new-research
    Click Button  Add Tag
    Click Button  Add
    Check page contains citation  Matti Luukkainen  Three years of design-based research to reform a software engineering curriculum  ACM  2012  new-research

Citation with invalid DOI should show error message
    Go To  ${HOME_URL}
    Click Link  New citation
    Input Text  doi-fetch  https://doi.org/10.1145/invalid
    Execute JavaScript  document.getElementById('doi-fetch').blur()
    Wait Until Page Contains  DOI not found!
    Sleep  1s
    Page Should Contain  DOI not found!
