*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations
Library   OperatingSystem

*** Keywords ***
Add Citation
    [Arguments]  ${citation_type}  ${author}  ${title}  ${publisher}  ${year}
    Go To  ${HOME_URL}
    Click Link  Create new citation
    Select From List By Value  citation_type  ${citation_type}
    Input Text  author      ${author}
    Input Text  title       ${title}
    Input Text  publisher   ${publisher}
    Input Text  year        ${year}
    Click Button  add_citation_button

*** Test Cases ***
At start there are no citations
    Go To  ${HOME_URL}
    Title Should Be  Citations app
    Page Should Contain  No citations.

First citation can be added
    Add Citation  book  John Doe  Aku Ankka  Otava  2000
    Page Should Contain  John Doe  Aku Ankka
    Page Should Contain  Otava  2000

Second citation can be added
    Add Citation  book   John Doe   Aku Ankka   Otava   2000
    Add Citation  article   Mary Jane  Minni Hiiri  Tammi   2003

    Page Should Contain  John Doe  Aku Ankka
    Page Should Contain  Otava  2000
    Page Should Contain  Mary Jane  Minni Hiiri
    Page Should Contain  Tammi  2003