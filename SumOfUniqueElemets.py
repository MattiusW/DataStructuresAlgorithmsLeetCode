"""
You are given an integer array nums. 
The unique elements of an array 
are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums.
"""

from typing import List
from collections import defaultdict

def sumOfUnique(nums: List[int]) -> int:
    ans = 0
    dic = defaultdict(int)

    for i in nums:
        dic[i] += 1

    for value in dic:
        if dic[value] == 1:
            ans += value

    return ans

def main():
    nums = [1,2,3,2]
    nums2 = [1,1,1,1,1]
    nums3 = [1,2,3,4,5]

    print(sumOfUnique(nums))
    print(sumOfUnique(nums2))
    print(sumOfUnique(nums3))
    

if __name__ == "__main__":
    main()