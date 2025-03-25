import math

def maxMinSelect(numbers):
    if len(numbers) == 1:
        return [numbers[0], numbers[0]] # base case

    middle = math.floor(len(numbers) / 2)

    max_min_left = maxMinSelect(numbers[:middle])
    max_min_right = maxMinSelect(numbers[middle:])

    # returns the max value and the min value as an array in the format: [max, min]
    return [max(max_min_left[0], max_min_right[0]), min(max_min_left[1], max_min_right[1])]

arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]
arr3 = [22, 31, 0, 4, 55]
arr4 = [22, 31, -55, 0, 4, 55]

maxmin1 = maxMinSelect(arr1)
maxmin2 = maxMinSelect(arr2)
maxmin3 = maxMinSelect(arr3)
maxmin4 = maxMinSelect(arr4)

print("Numbers: " + str(arr1) + "\n\tMax:" + str(maxmin1[0]) + "\n\tMin:" + str(maxmin1[1]))
print("Numbers: " + str(arr2) + "\n\tMax:" + str(maxmin2[0]) + "\n\tMin:" + str(maxmin2[1]))
print("Numbers: " + str(arr3) + "\n\tMax:" + str(maxmin3[0]) + "\n\tMin:" + str(maxmin3[1]))
print("Numbers: " + str(arr4) + "\n\tMax:" + str(maxmin4[0]) + "\n\tMin:" + str(maxmin4[1]))