from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
        ans = 0.0
        curr = 0.0

        for i in range(k):
            curr += nums[i]

        ans = curr

        for j in range(k, len(nums)):
            curr = curr + nums[j] - nums[j - k]
            ans = max(ans, curr)

        return ans / k
        
def main():
    print("Maximum Average Subarray")
    
    print(findMaxAverage(nums=[3,3,4,3,0], k=3))

if __name__ == "__main__":
    main()