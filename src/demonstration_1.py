"""
Given a list of integers and a target value, return the indices of the two numbers in the list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, and the same element cannot be used more than once.*

Example:

Given nums = [3, 8, 12, 17], target = 15,

Because nums[0] + nums[2] = 3 + 12 = 15,
return [0, 2].
"""

# how do we return the index and not the value
# iterate over nums list using range so that we have access to the indices
    # check if the current number + any of the rest of the numbers == target
    # use another loop to go over the rest of the numbers:
        # sum them up and compare against the target
        # if they're equal:
            # grab their indices and return them as a list [num1, num2]

def twoSum(nums, target):

	for i in range(len(nums)):
		for j in range(i, len(nums)):
			sum = nums[i] + nums[j]
			if sum == target:
				return [i, j]

print(twoSum([3, 8, 12, 17], 15))











# def two_sum(nums, target):
#     for i in range(len(nums)-1):
# 		a = nums[i]
# 		for j in range(i+1, len(nums)):
# 			b = nums[j]
# 			if a + b == target:
# 				return [a, b]
# 	return []

# nums = [3, 8, 12, 17]
# target = 15
# print(two_nums(nums, target))

# def twoNumberSum(array, targetSum):
# 	nums ={}
# 	for num in array:
# 		potentialMatch = targetSum - num
# 		if potentialMatch in nums:
# 			return [potentialMatch, num]
# 		else: nums[num] = True
# 	return []

