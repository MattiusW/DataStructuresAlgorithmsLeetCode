"""
In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. Each number was supposed to appear exactly once in the list, however, 
two mischievous numbers sneaked in an additional time, making the list longer than usual.
As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.
"""

from typing import List
from collections import defaultdict

def getSneakyNumbers(nums: List[int]) -> List[int]:
    ans = []
    dic = defaultdict(int)

    for i in nums:
        dic[i] += 1

    for value in dic:
        if dic[value] == 2:
            ans.append(value)

    return sorted(ans)

def main():
    
    nums1 = [0,1,1,0] # [0,1]
    nums2 = [0,3,2,1,3,2] # [2,3]
    nums3 = [7,1,5,4,3,4,6,0,9,5,8,2] #[4,5]

    print(getSneakyNumbers(nums1))
    print(getSneakyNumbers(nums2))
    print(getSneakyNumbers(nums3))

if __name__ == "__main__":
    main()