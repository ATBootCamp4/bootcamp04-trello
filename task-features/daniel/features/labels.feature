Feature: Trello labels API
    As a user I want to work with labels in the API
    
      Scenario: Create and modify label from board
        Given the user wants to create a label
        |key  |value   |
        |board|QI9piQFl|
        |name |nombre  |
        |color|blue    |
        When the user modifies the label with
        |key  |value          |
        |name |nombre_cambiado|
        |color|green          |
        Then verifies the data to be correct
