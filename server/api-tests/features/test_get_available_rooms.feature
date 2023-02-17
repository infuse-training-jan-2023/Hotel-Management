
Feature: Get available rooms
  As a customer I want to get list of all rooms available

  Scenario: Get available rooms
    When i try to search for rooms  
    Then i should get the rooms available based on filters
    Then the api status code should be 201
    Then the api response content type should be json