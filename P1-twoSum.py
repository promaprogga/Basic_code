# nums = []
# n = int(input("Number of elements in array:"))
# for i in range(0, n):
#     l = int(input())
#     nums.append(l)
# # print("numms = ",nums)
#
# target = int(input())
# # print(target)
#
# if(len(nums)>=2):
#    for i in range(len(nums)-1):
#       t=nums[i] + nums[i + 1]
#       if(t==target):
#            print(i,i+1)
#
# else:
#     print("No exists")


# Brute Force
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


# Two-pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]


# One-pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
