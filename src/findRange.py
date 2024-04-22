#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
   Find the range
   '''
def find_range(numbers):
   # TODO: create the variable `lowest` and assign it to the smallest value of the `numbers` list, using the function `min()`
   # TODO: create the variable `highest` and assign it to the largest value of the `numbers` list , using the function `max()`
   # Find the range
   # TODO: determine the difference between `highest` and `lowest`. Assign this value to the value `r`
   return lowest, highest, r
# end of find_range()

if __name__ == '__main__':
   donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
   lowest, highest, r = find_range(donations)
   print('Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, r))
