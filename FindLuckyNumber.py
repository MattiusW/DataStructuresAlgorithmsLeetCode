from collections import defaultdict
from typing import List

def findLucky(arr: List[int]) -> int:
    ans = 0
    dic = defaultdict(int)

    for i in arr:
        dic[i] += 1

    for value in dic:
        if value == dic[value]:
            ans = max(ans, value)

    return ans if ans != 0 else -1

def main():
    arr = [2,2,3,4]
    arr2 = [1,2,2,3,3,3]
    arr3 = [2,2,2,3,3]

    anserw1 = findLucky(arr=arr)
    anserw2 = findLucky(arr=arr2)
    anserw3 = findLucky(arr=arr3)

    print(anserw1)
    print(anserw2)
    print(anserw3)

if __name__ == "__main__":
    main()