class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#       Solution uses hashmap
        hm = {}

        for word in strs:
            abc_order = "".join(sorted(word))

            if abc_order in hm:
                hm[abc_order].append(word)
            else:
                hm[abc_order] = [word]

        return list(hm.values())
