from collections import defaultdict

def numJewelsInStones(jewels: str, stones: str) -> int:
    dic = defaultdict(int)
    ans = 0
        
    for i in stones:
        dic[i] += 1
        
    for j in range(len(jewels)):
        if jewels[j] in dic:
            ans += dic.get(jewels[j])

    return ans
            
def main():
    example1 = numJewelsInStones(jewels="aA", stones="aAAbbbb")
    
    print(example1)

if __name__ == "__main__":
    main()