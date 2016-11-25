# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.


# NOTE: the solution below does not account for self cycle which mean 2 identical values next to each other. Example: 1, 2, 3, 3, 4
def findDuplicate(self, nums):
    fast = 0
    slow = 0
    finder = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[slow]]
        if slow == fast:
            break

    while True:
        slow = nums[slow]
        finder = nums[finder]
        if slow == finder:
            return slow