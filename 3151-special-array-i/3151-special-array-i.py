class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all(map(lambda n:sum(n)%2, pairwise(nums)))
        