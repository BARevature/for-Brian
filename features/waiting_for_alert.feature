Feature: You can tell Selenium to wait for elements that take a while to become intractable
  Scenario: As a user, I need to wait three seconds to interact with an alert after pressing a button
    Given I am on the webpage with the button
    When  I click the button
    Then  I should see an alert with my message after 3 seconds
    Then  I should not be able to see the button anymore