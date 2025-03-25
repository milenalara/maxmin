import math

def maxMinSelect(numbers):
    if len(numbers) == 1:
        return [numbers[0], numbers[0]] # base case

    middle = math.floor(len(numbers) / 2)

    max_min_left = maxAndMin(numbers[:middle])
    max_min_right = maxAndMin(numbers[middle:])

    # returns the max value and the min value as an array in the format: [max, min]
    return [max(max_min_left[0], max_min_right[0]), min(max_min_left[1], max_min_right[1])]