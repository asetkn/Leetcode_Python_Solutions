class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Solution using hashmap
        hashm = {}
        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashm:
                return [hashm[diff], i]

            hashm[n] = i
