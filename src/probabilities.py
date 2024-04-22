#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This example defines a six-sided die using FiniteSet and calculates the probability of getting an even number or a number greater than 4. The calculate_probability function is used to compute the probability of an event based on the number of favorable outcomes and the total number of possible outcomes. The Rational class from sympy is used to represent exact fractions to maintain precision in the probability calculations.

# Note: you will have to create a virtual environment to run this code.
# The commands are the following
# python3 -m venv ~/Desktop/myVenv # Unix
# python -m venv c:\YOUR_PATH\myVenv # Windows
#
# Run source to start the virtual environment
# source ~/Desktop/myVenv/bin/activate # Unix
# c:\YOUR_PATH\myVenv\scripts\activate # Windows
#
# Install Sympy library with pip once the virtual environment has started
# pip install sympy
# Now, run your code

# TODO fix the error in the import statement blow to run the code
# FROM sympy IMPORT FiniteSet, and Rational


def calculate_probability(outcomes, total_outcomes):
    """ Function to use lengths of sets to determine probability"""
    return Rational(len(outcomes), total_outcomes) # return a fraction
# end of calculate_probability()

# Define a six-sided die
die_outcomes = FiniteSet(1, 2, 3, 4, 5, 6)

# Choose an event, for example, getting an even number
# TODO: Create the variable `even_numbers` and assign it to the built-in function `FiniteSet()` with the parameters of the three even values of a die 

# Calculate and display the probability of getting an even number
probability_even_numbers = calculate_probability(even_numbers, len(die_outcomes))

# Choose another event, for example, getting a number greater than 4
# TODO: Create the variable `numbers_greater_than_4` and assign it to the built-in function `FiniteSet()` with the parameters of all values of a die that are strictly greater than four 

# Calculate and display the probability of getting a number greater than 4
probability_greater_than_4 = calculate_probability(numbers_greater_than_4, len(die_outcomes))

print(f"Probability of getting an even number: {probability_even_numbers}, greater than 4: {probability_greater_than_4}")
