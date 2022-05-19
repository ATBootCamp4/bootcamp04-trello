#cual es el objetivo de las pruebas
Feature: Trello labels API
    As a user I want to work with labels in the API

  Scenario: Get data from specific label
     Given the user does a GET request to /labels/id endpoint
      When the user sends the request
      Then verify the status code is 200
      And that the given label exists

  Scenario Outline: Create label in board
     Given the user wants to create new label
     When the user sends a POST request with "<name"> and "<color2>"
     Then verify the status code is 200
     And verify that the new label exists with the exact data
     Examples: new_label
      | name2   | color2 |
      | paco    | orange |

  Scenario: Delete label from board 
    Given the user wants to DELETE a label
     When the user sends DELETE request
     Then verify the status code is 200
     And verify that label dont exists anymore in board

  Scenario Outline: Modify data from specific label
     Given the user wants to change the data in a label
     When the user sends PUT request with "<name2>" and "<color2>"
     Then verify the status code is 200
     And verify that the label has the new name and color
     Examples: new_data
      | name   | color |
      | manolo | green |


