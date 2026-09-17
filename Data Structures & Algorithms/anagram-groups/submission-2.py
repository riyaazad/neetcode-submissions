class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            final[sortedS].append(s)
        return list(final.values())
            