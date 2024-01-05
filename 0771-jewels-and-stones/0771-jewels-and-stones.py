class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash = collections.defaultdict(int)
        count = 0

        for char in stones:
            hash[char] += 1

        for char in jewels:
            count += hash[char]
            
        return count