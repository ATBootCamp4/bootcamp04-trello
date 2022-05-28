Feature: Trello labels API
    As a user I want to work with labels in the API

#SCENARIO I
 Scenario: Create and verify label in board
    Given I send a "POST" request to "boards/{board}/labels"
            | Key    | Value        | 
            | name   | Checklist 1  |
            | color  | green        |
    Then the status code is "200"
    When I send a "GET" request to "labels/{response}"
    Then I check the data is
            | Key    | Value        | 
            | name   | Checklist 1  |
            | color  | green        |

    
#SCENARIO II
 Scenario: Get all labels in a board
     Given I send a "POST" request to "boards/{board}/labels"
            | Key    | Value        | 
            | name   | label 2      |
            | color  | green        |
    When I send a "GET" request to "boards/{board}/labels"
    And the status code is "200"
    Then I receive a response with the "labels_on_board" schema
    Then I receive a list with at least "1" "label"



#SCENARIO III
Scenario Outline: Create labels in specific card with different names and colors
      Given I created a new card
      When I send a "POST" request to "/cards/{card}/labels"
            | Key    | Value        | 
            | name   | <Name>       |
            | color  | <Color>      |
      And the status code is "<http_response>"
      Then I check the data is
            | Key    | Value        | 
            | name   | <Name>       |
            | color  | <Color>      |        
        Examples: Values
        |Name   |Color     |http_response   |
        |  aaa  |  green   |  200           |
        |  ,,,  |  yellow  |  200           |
        | 111   |  orange  |  200           |
 
#SCENARIO IV  
   Scenario: Modify data from specific label
    Given I send a "POST" request to "boards/{board}/labels"
            | Key    | Value        | 
            | name   |  original    |
            | color  | yellow       |
     When  I send a "PUT" request to "labels/{response}"
            | Key    | Value        | 
            | name   | changed      |
            | color  | blue         |
    And I send a "GET" request to "labels/{response}"
    Then I check the data is
            | Key    | Value        | 
            | name   | changed      |
            | color  | blue         |

# # SCENARIO V 
    Scenario: DELETE label from board
        Given I send a "POST" request to "boards/{board}/labels"
            | Key    | Value        | 
            | name   |  a_borrar    |
            | color  | sky          |
        And the status code is "200"
        Then the item id is saved before deletion
        When I send a "DELETE" request to "/labels/{response}"
        And the status code is "200"
        Then I send a "GET" request to "/labels/{deleted_item}"
        And the status code is "404"

# #SCENARIO VI
    Given I created a new card
    When I send a "POST" request to "/cards/{card}/labels"
        | Key    | Value        |
        | name   | <Name>       |
        | color  | <Color>      |
    And the status code is "<http_response>"
    Then the response contains the message "error"
    Examples: Values
    |Name   |Color     |http_response   |
    |  aaa  |  ble     |  400           |
    |  ~    |  magenta |  400           |
