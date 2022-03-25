Feature: Multiple languages should be supported
  Scenario: As a user, I should be able to navigate to the apple fruit page when I type in apple to the search bar so I can learn more about the delicious fruit
    Given I am on the Wikipedia home page
    When  I enter apple into the search bar
    When  I select English as my search language
    When  I click the search button
    Then  I should be sent to the apple fruit information page

  Scenario: As a user, I should be able to navigate to the Apple tech company home page when I type in apple to the search bar and search in the Spanish language
    Given I am on the Wikipedia home page
    When  I enter apple into the search bar
    When  I select Spanish as my search language
    When  I click the search button
    Then  I should be sent to the Apple tech company information page