Feature: get booking records
    As a customer I can get booking records

    Scenario: get booking records
        When I select on profile
        Then I should get list of booking records
        Then the api status code should be 200
        Then the api response type should be json