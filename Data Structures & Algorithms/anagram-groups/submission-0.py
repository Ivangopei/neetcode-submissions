class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)          # sorted letters -> original words
        for word in strs:
            key = tuple(sorted(word)) # sorted() returns a list; lists can't be keys
            groups[key].append(word)
        return list(groups.values())