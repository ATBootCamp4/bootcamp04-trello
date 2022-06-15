Feature: Trello UI Login
    As a User I want to be able to log in to the app

    Scenario: Log in to app
        Given the user send its username to "username input"
        And the user waits for "password input" to disapear
        When the user presses the "login button"
        And the user send its password to "password input"
        And the user presses the "submit loggin button"
        Then the user is logged in

