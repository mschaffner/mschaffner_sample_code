'''
Problem source: https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

from collections import namedtuple
Trap = namedtuple('Trap', ['start_index', 'start_height', 'end_index'])

def calculate_rainwater(elevation_map):
    total_trapped_water = 0
    water_holes = []
    last = None

    for i, height in enumerate(elevation_map):
        if last is None:
            last = height

        if height > last:
            for j, trap in enumerate(water_holes):
                if height >= trap.start_height and trap.end_index is None:
                    trap = water_holes[j] = trap._replace(end_index=i - 1)
                    total_trapped_water += trap.end_index - trap.start_index
        elif height == last:
            continue
        else:
            water_holes.append(Trap(i - 1, last, None))

        last = height
    return total_trapped_water

def test_calculate_rainwater():
    # Provided example, jagged
    t = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert 6 == calculate_rainwater(t), "Incorrect answer returned"

    # No traps, all downhill
    t = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert 0 == calculate_rainwater(t), "Incorrect answer returned"

    # No traps, all uphill
    t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert 0 == calculate_rainwater(t), "Incorrect answer returned"

    # V shaped
    t = [5, 4, 3, 2, 1, 2, 3, 4, 5]
    assert 16 == calculate_rainwater(t), "Incorrect answer returned"

    print "All tests passed :)"

if __name__ == "__main__":
    test_calculate_rainwater()
