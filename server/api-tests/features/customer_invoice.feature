Feature: Download Invoice
    As a Customer i can download the invoice

    Scenario: Download Invoice
        When Customer click Download Invoice
        Then Customer can see Invoice 
        Then Api status code should be 200
        Then Api response content type should be application/pdf