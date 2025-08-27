Feature: E2E magento

  Scenario: E2E_magento
    Given Navigate to the website magento.softwaretestingboard.com
    Then Click on the following button Consent
    Then Click on the following button Create an Account
    Then Fill the following fields
      | field_name       | value              |
      | First Name       | Maria              |
      | Last Name        | Lucia              |
      | Email            | Maria1111@gmail.com |
      | Password         | @123411mk          |
      | Confirm Password | @123411mk          |
    Then Click on the following submit button Create an Account
    Then Click on the following button Edit