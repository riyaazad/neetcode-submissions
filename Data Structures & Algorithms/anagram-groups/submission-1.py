class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list) #creates an empty list automatically which is why we passed list as param
        for str in strs:
            sortedS = ''.join(sorted(str))
            final[sortedS].append(str)  #look at key sortedS and add s to it if it matches
            #each key in final is a sorted versiona of a work
            #each value is a list of words that match the key
        return  list(final.values()) #list() is a built in constructor


        