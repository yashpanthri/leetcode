class Solution:
    def ret_tup_word(self, word):
        ret_tup = [0]*26
        for i in range (len(word)):
            ret_tup[ord(word[i]) - ord('a')] +=1
        return tuple(ret_tup)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for i in range(len(strs)):
            key = self.ret_tup_word(strs[i])
            if not key in answer:
                answer[key] = [strs[i]]
            else:
                answer[key].append(strs[i])
        result = []
        for key in answer:
            result += [answer[key]]
        return result