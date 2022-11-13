class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#       Solution uses hashmap
        hm = {}

        for val in set(nums):
            val_count = nums.count(val)
            if val_count in hm:
                temp_list = hm[val_count]
                temp_list.append(val)
                hm[val_count] = temp_list
            else:
                hm[val_count] = [val]

        hm_keys = list(hm.keys())
        hm_keys.sort(reverse=True)
        k_elements = []

        for key in hm_keys[:k]:
            if len(k_elements) >= k:
                break 
            elif len(hm[key]) == k:
                k_elements = hm[key]
                break
            else: 
                k_elements.extend(hm[key])

        return k_elements
