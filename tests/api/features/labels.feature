Feature: Trello labels API
    As a user I want to work with labels in the API

#SCENARIO I
 Scenario: Create and verify label in board
    When I send a "POST" request to "boards/{board}/labels?"
            | Key    | Value        | 
            | name   | Checklist 1  |
            | color  | green        |
    And the status code is "200"
    And I get the item info
    Then I check data
    
# SCENARIO II
 Scenario: Get all labels in a board
    When I send a "GET" request to "boards/{board}/labels?"
    And the status code is "200"
    Then I receive a list with at least "1" "label"

#SCENARIO III

Scenario Outline: Create labels in specific card with different names
      Given I created a new card
      When I send a "POST" request to "/cards/{card}/labels"
            | Key    | Value        | 
            | name   | <Name>       |
            | color  | <Color>      |
      And the status code is "<http_response>"
    Examples: Values
    |names  |colors    |http_response   |
    |  aaa  |  green   |  200           |
    |  ,,,  |  yellow  |  200           |
    |  ---  |  blue    |  200           |
    | 111   |  orange  |  200           |
 
#SCENARIO IV  
  Scenario: Modify data from specific label
    When I send a "POST" request to "boards/{board}/labels?"
            | Key    | Value        | 
            | name   |  original    |
            | color  | yellow       |
     And I get the item info
     And the user sends PUT request with "ionolo" and "green"
     And the status code is "200"
     Then I check data
    
