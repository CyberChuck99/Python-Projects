# Two Sum: return the indices of the two numbers that add up to the target.

def two_sum(nums, target):
    seen = {}  # maps a number to the index where we saw it
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return seen[need], i
        seen[n] = i
    return None  # outdented: only runs after the whole list has been checked


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # (0, 1)
print(two_sum(nums, 100))     # None
