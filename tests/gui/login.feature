Feature: Trello UI Login
    As a User I want to be able to log in to the app

    Scenario: Log in to app
        Given the user goes to "/login"
        When the user sends its credentials
        Then the user should be logged in 

