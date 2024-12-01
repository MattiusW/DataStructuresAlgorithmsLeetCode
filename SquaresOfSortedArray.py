from typing import List

def sortedSquares(nums: List[int]) -> List[int]:

    for j in range(len(nums)):
        nums[j] *= nums[j]
    
    nums.sort()

    return nums


def main():
    nums_not_sorted = [-4,-1,0,3,10]

    print("Squares of Sorted Array Leet Code:")
    print(f"Orginal nums: {nums_not_sorted}")

    sorted_squares_nums = sortedSquares(nums=nums_not_sorted)

    print(f"Sorted and Squares nums: {sorted_squares_nums}")

if __name__ == "__main__":
    main()