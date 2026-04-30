"""Tests for sci_units.converters.

Two of these tests will fail against the starter implementation. The Block 1
demo asks the AI agent to find and fix the bug.
"""

import pytest
from sci_units.converters import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
)


def test_fahrenheit_to_celsius_freezing():
    assert fahrenheit_to_celsius(32) == pytest.approx(0.0)


def test_fahrenheit_to_celsius_boiling():
    assert fahrenheit_to_celsius(212) == pytest.approx(100.0)


def test_celsius_to_fahrenheit_round_trip():
    assert celsius_to_fahrenheit(fahrenheit_to_celsius(75)) == pytest.approx(75.0)


def test_kelvin_to_celsius_absolute_zero():
    assert kelvin_to_celsius(0) == pytest.approx(-273.15)
