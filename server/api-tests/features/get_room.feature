
Feature: Get room details
  As a customer I can get the details of a room

  Scenario: Get room details
    When I select a room 
    Then I should get all the details of the room
    Then the api status code should be 200
    Then the api response content type should be json