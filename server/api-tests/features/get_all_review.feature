Feature: All Customer Reviews
    As a Customer i can view all Hotel room reviews

    Scenario: All Customer Reviews
        When Customer View Room
        Then Customer can see All Customer reviews
        Then Api status code should be 200