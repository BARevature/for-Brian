Feature: I can parameterize my scenarios using a scenario outline
  Scenario Outline: as a wiki user, I can search multiple different topics on wikipedia
    Given I am on the Wikipedia home page
    When  I type <criteria> into the search bar
    When  I click the search button
    Then  I should be sent to a page with <title> as the title
    Examples:
      | criteria | title            |
      | fish     | Fish - Wikipedia |
      | cat      | Cat - Wikipedia  |
      | dog      | Dog - Wikipedia  |