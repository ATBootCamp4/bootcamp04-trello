Feature: Trello API Attachments
    As a user
    I want "Attachments" API endpoints
    In order to manipulate attachments

    @smoke
    Scenario: GET all attachments from a card
        Given I created a new card
        And I created an attachment on the card
        When I send a "GET" request to "/cards/{card}/attachments"
        Then I receive a list with at least "1" "attachment"
        And I receive a response with the "get_attachments" schema
        And the status code is "200"

    Scenario: GET an attachment from a card
        Given I created a new card
        And I created an attachment on the card
        When I send a "GET" request to "/cards/{card}/attachments/{attachment}"
        Then I receive a response with the "attachment" schema
        And the status code is "200"

    @negative
    Scenario: GET an non existing attachment from a card
        Given I created a new card
        And I created an attachment on the card
        When I send a "GET" request to "/cards/{card}/attachments/X"
        Then the response contains the message "invalid"
        And the status code is "400"

    Scenario Outline: POST an attachment to a card from an url
        Given I created a new card
        When I send a "POST" request to "/cards/{card}/attachments"
            | Key      | Value   |
            | url      | <URL>   |
            | name     | <Name>  |
            | setCover | <Cover> |
        Then the attachment is created on the card
        And I receive a response with the "attachment" schema
        And the status code is "200"

    Examples:
        | URL                                            | Name          | Cover | comment                             |
        | https://www.svgrepo.com/show/354463/trello.svg | Trello logo   | false | normal image attachment             |
        | fpt.aaa.bbb.ccc                                | invalid       | false | API adds "http://" and returns 200  |
        | https://source.unsplash.com/user/c_v_r         | cover         | true  | cover image attachment              |

    @negative
    Scenario: POST a non-image attachment as cover to a card
        Given I created a new card
        When I send a "POST" request to "/cards/{card}/attachments"
            | Key      | Value                                     |
            | url      | https://panasonickitchen.com/robots.txt   |
            | name     | Text                                      |
            | setCover | true                                      |
        Then the response contains the message "failed"
        And the status code is "400"


    @smoke
    Scenario: DELETE an attachment from a card
        Given I created a new card
        And I created an attachment on the card
        When I send a "DELETE" request to "/cards/{card}/attachments/{attachment}"
        Then I receive a response with the "delete" schema
        And the status code is "200"
    