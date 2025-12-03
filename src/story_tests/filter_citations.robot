*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations
Library   OperatingSystem


*** Test Cases ***
Search with non-matching query should return no citations
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Add citation  book  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008
    Input Text  query  asdasd
    Sleep  1s
    Page Should Contain  No citations.


Search with matching query should return citation
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Add citation  book  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008
    Input Text  query  ref
    Sleep  1s
    Page Should Contain  Martin Fowler
    Page Should Contain  Refactoring: Improving the Design of Existing Code
    Page Should Contain  Addison-Wesley
    Page Should Contain  1999
    Page Should Not Contain  Clean Code: A Handbook of Agile Software Craftsmanship