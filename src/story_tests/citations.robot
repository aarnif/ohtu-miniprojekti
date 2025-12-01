*** Settings *** 
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations
Library   OperatingSystem

*** Keywords *** 
Add Citation
    [Arguments]  ${author}  ${title}  ${publisher}  ${year}
    Go To  ${HOME_URL}
    Click Link  Create new citation
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
    Add Citation  John Doe  Aku Ankka  Otava  2000
    Page Should Contain  John Doe  Aku Ankka
    Page Should Contain  Otava  2000

Second citation can be added
    Add Citation  John Doe   Aku Ankka   Otava   2000
    Add Citation  Mary Jane  Minni Hiiri  Tammi   2003
    Page Should Contain  John Doe  Aku Ankka
    Page Should Contain  Otava  2000
    Page Should Contain  Mary Jane  Minni Hiiri
    Page Should Contain  Tammi  2003

Citation can be downloaded
    Go To  ${HOME_URL}
    Click Button  Download BibTeX File
    IF  $HOME_PATH == '/home/runner'
        ${FILE_PATH}=  Set Variable  /home/runner/ohtu-miniprojekti/ohtu-miniprojekti/exported_citations.bib
    ELSE
        ${FILE_PATH}=  Set Variable  ${HOME_PATH}/Downloads/exported_citations.bib
    END
    File Should Exist  ${FILE_PATH}
    ${downloaded_text}=  Get File  ${FILE_PATH}
    Should Contain  ${downloaded_text}  John Doe  Aku Ankka
    Should Contain  ${downloaded_text}  Mary Jane  Minni Hiiri