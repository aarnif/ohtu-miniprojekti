*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations
Library   OperatingSystem


*** Test Cases ***
Search with non-matching query should return no citations
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613
    Add citation  book  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008  10.1145/1869452.1869473
    Input Text  query  asdasd
    Sleep  1s
    Page Should Contain  No citations.


Search with matching query should return citation
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613
    Add citation  book  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008  10.1145/1869452.1869473
    Input Text  query  ref
    Sleep  1s
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Page Should Not Contain  Clean Code: A Handbook of Agile Software Craftsmanship

Search with number 20 should return all citations from years 2000-2025
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613
    Add citation  book  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008  10.1145/1869452.1869473
    Add citation  book  Eric Evans  Domain-Driven Design: Tackling Complexity in the Heart of Software  Addison-Wesley  2003  10.1145/1234567.1234568
    Input Text  query  20
    Sleep  1s
    Check page contains citation  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008
    Check page contains citation  Eric Evans  Domain-Driven Design: Tackling Complexity in the Heart of Software  Addison-Wesley  2003
    Page Should Not Contain  Refactoring: Improving the Design of Existing Code

Search with matching doi should return citation
    Add citation  book  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999  10.1145/2380552.2380613
    Add citation  book  Robert C. Martin  Clean Code: A Handbook of Agile Software Craftsmanship  Prentice Hall  2008  10.1145/1869452.1869473
    Add citation  book  Eric Evans  Domain-Driven Design: Tackling Complexity in the Heart of Software  Addison-Wesley  2003  10.1145/1234567.1234568
    Input Text  query  https://doi.org/10.1145/2380552.2380613
    Sleep  1s
    Check page contains citation  Martin Fowler  Refactoring: Improving the Design of Existing Code  Addison-Wesley  1999
    Page Should Not Contain  Clean Code: A Handbook of Agile Software Craftsmanship
    Page Should Not Contain  Domain-Driven Design