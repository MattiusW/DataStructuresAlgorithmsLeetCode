from collections import defaultdict
from typing import List

def maxFrequencyElement(nums: List[int]) -> int:
    ans = 0
    dic = defaultdict(int)

    for i in nums:
        dic[i] += 1

    for value in dic:
        if dic[value] == max(dic.values()):
            ans += max(dic.values())

    return ans

def main():
    nums = [1,2,2,3,1,4] # 4
    nums2 = [1,2,3,4,5] # 5

    example1 = maxFrequencyElement(nums=nums) 
    example2 = maxFrequencyElement(nums=nums2)

    print(example1)
    print(example2)

if __name__ == "__main__":
    main()