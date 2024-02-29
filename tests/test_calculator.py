# pytest-bdd uses pytest native syntax for declaring scenarios
import pytest
from pytest_bdd import scenario, given, when, then, parsers
import sys
from pathlib import Path

# Add the project root directory to the Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

@scenario('calculator.feature', 'Add two numbers')
def test_add():
    pass

@scenario('calculator.feature', 'Subtract two numbers')
def test_subtract():
    pass

@scenario('calculator.feature', 'Multiply two numbers')
def test_multiply():
    pass

@given('the calculator is run')
def run_calculator(calc):
    pass

@when(parsers.cfparse('I add {number1:d} and {number2:d}'))
def add_numbers(calc, number1, number2):
    calc.result = calc.add(number1, number2,)

@when(parsers.cfparse('I subtract {number2:d} from {number1:d}'))
def subtract_numbers(calc, number1, number2):
    calc.result = calc.subtract(number1, number2)

@when(parsers.cfparse('I multiply {number1:d} and {number2:d}'))
def multiply_numbers(calc, number1, number2):
    calc.result = calc.multiply(number1, number2)

@then(parsers.cfparse('the result should be {result:d}'))
def result_should_be(calc, result):
    assert calc.result == result

