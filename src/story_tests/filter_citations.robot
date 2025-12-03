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