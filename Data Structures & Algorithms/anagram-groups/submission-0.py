class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            sortedWord = "".join(sorted(s))
            groups[sortedWord].append(s)
        return list(groups.values())
        