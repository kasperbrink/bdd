Feature: Simple Calculator
  In order to avoid silly mistakes
  As a math enthusiast
  I want to be able to perform basic arithmetic operations

  Scenario Outline: Add two numbers
    Given the calculator is run
    When I add <number1> and <number2>
    Then the result should be <result>

    Examples:
      | number1 | number2 | result |
      | 10      | 20      | 30     |
      | 1       | 99      | 100    |

  Scenario Outline: Subtract two numbers
    Given the calculator is run
    When I subtract <number2> from <number1>
    Then the result should be <result>

    Examples:
      | number1 | number2 | result |
      | 30      | 10      | 20     |
      | 100     | 1       | 99     |
  
  Scenario Outline: Multiply two numbers
    Given the calculator is run
    When I multiply <number1> and <number2>
    Then the result should be <result>

    Examples:
      | number1 | number2 | result |
      | 5       | 2       | 10     |
      | 10      | 10      | 100    |