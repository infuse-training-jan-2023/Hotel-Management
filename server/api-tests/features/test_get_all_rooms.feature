
Feature: Get all rooms
  As a customer I want to get list of all rooms 

  Scenario: Get all rooms
    When i try to get list rooms  
    Then i should get all the rooms
    Then the api status code should be 200
    Then the api response content type should be json