Feature: book room
    As a user i can book a room

    Scenario: book room
        When I book a room
        Then I should get confirmation message
        Then The api status code should be 201
        Then The api Response type should be json