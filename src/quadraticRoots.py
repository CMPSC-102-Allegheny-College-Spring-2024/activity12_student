#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc_quad_eqn_roots(
a: float, b: float, c: float) -> float:
    """Calculate roots of quadratic equation."""
    # TODO: Create a variable, `D` and set it equal to `b^2 - 4*a*c`
    # TODO: Set D to the square root of itself
    x_one = (-b + D) / (2 * a)
    x_two = (-b - D) / (2 * a)
    # TODO: return the two variables which are calculated here.

print(f"{calc_quad_eqn_roots(1,2,1)}")
