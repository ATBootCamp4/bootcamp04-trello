#cual es el objetivo de las pruebas
Feature: Trello labels API
    As a user I want to work with labels in the API

#SCENARIO I
#   Scenario: Get data from specific label
#     Given the user does a GET request to /labels/id endpoint
#      When the user sends the request
#      Then verify the status code is 200
#      And that the given label exists
#      And validate the schema


# SCENARIO II
#  Scenario: Create label in board
#     Given the user wants to create new "red" label named "pauico"
#     When the user sends a POST request with the data
#     Then verify the status code is 200
#     And verify that the new label named "pauico" is "red"


#SCENARIO III
#  Scenario: Delete label from board 
#    Given the user wants to DELETE a label
#     When the user sends DELETE request
#     Then verify the status code is "200"
#     And verify that label dont exists anymore in board

#SCENARIO IV  
#  Scenario: Modify data from specific label
#     Given the user wants to change the data in a label
#     When the user sends PUT request with "ionolo" and "green"
#     Then verify the status code is "200"
#     And verify that the label is named "ionolo" and is "green"

#SCENARIO V
    # Scenario: Create and modify label from board
    #   Given the user wants to create a label
    #   |key  |value   |
    #   |board|QI9piQFl|
    #   |name |nombre  |
    #   |color|blue    |
    #    When the user modifies the label with
    #    |key  |value          |
    #    |name |nombre_cambiado|
    #    |color|green          |
    #    Then verifies the data to be correct

#SCENARIO VI

Scenario Outline: Create labels in specific card with different names
    Given the user creates labels in a card with different "<names>" and "<colors>"
     When the user do the request
     Then verify the status code is "<http_response>"
    Examples: Values
    |names  |colors    |http_response   |
    |  aaa  |  green   |  200           |
    |  ,,,  |  yellow  |  200           |
    |  ---  |  blue    |  200           |
    | 111   |  orange  |  200           |
