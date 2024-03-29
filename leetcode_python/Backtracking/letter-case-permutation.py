"""

Given a string s, we can transform every letter individually to be lowercase 
or uppercase to create another string.
Return a list of all possible strings we could create. You can return the output in any order.

 
Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

Example 3:

Input: s = "12345"
Output: ["12345"]

Example 4:

Input: s = "0"
Output: ["0"]
 

Constraints:

s will be a string with length between 1 and 12.
s will consist only of letters or digits.

"""

# V0 
# IDEA : DFS 
class Solution(object):
    def letterCasePermutation(self, S):
        res = []
        self.dfs(S, res, "")
        return res
    
    def dfs(self, S, res, word):
        if not S:
            res.append(word)
            return
        if S[0].isalpha():
            self.dfs(S[1:], res, word + S[0].upper())
            self.dfs(S[1:], res, word + S[0].lower())
        else:
            self.dfs(S[1:], res, word + S[0])
            
# V0'
# IDEA : DFS
class Solution(object):
    def letterCasePermutation(self, S):
        r = []
        self.dfs(S, r, "")
        return r
    
    def dfs(self, S, r, tmp):
        if len(S) == 0:
            r.append(tmp)
            return
        if not S[0].isalpha():
            self.dfs(S[1:], r, tmp + S[0])    
        elif S[0].isalpha():
            self.dfs(S[1:], r, tmp + S[0].lower())
            self.dfs(S[1:], r, tmp + S[0].upper())
            
# V1 
# http://bookshadow.com/weblog/2018/02/18/leetcode-letter-case-permutation/
# IDEA : Recursion
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S: return [S]
        rest = self.letterCasePermutation(S[1:])
        if S[0].isalpha():
            return [S[0].lower() + s for s in rest] + [S[0].upper() + s for s in rest]
        return [S[0] + s for s in rest]

# V1'
# https://blog.csdn.net/fuxuemingzhu/article/details/79360330
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.dfs(S, 0, res, '')
        return res
    
    def dfs(self, string, index, res, path):
        if index == len(string):
            res.append(path)
            return
        else:
            if string[index].isalpha():
                self.dfs(string, index + 1, res, path + string[index].upper())
                self.dfs(string, index + 1, res, path + string[index].lower())
            else:
                self.dfs(string, index + 1, res, path + string[index])

# V1''
# https://blog.csdn.net/fuxuemingzhu/article/details/79360330
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.dfs(S, res, "")
        return res
    
    def dfs(self, S, res, word):
        if not S:
            res.append(word)
            return
        if S[0].isalpha():
            self.dfs(S[1:], res, word + S[0].upper())
            self.dfs(S[1:], res, word + S[0].lower())
        else:
            self.dfs(S[1:], res, word + S[0])

# V1'''
# https://blog.csdn.net/fuxuemingzhu/article/details/79360330
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for s in S:
            if s.isalpha():
                res = [word + j for word in res for j in [s.lower(), s.upper()]]
            else:
                res = [word + s for word in res]
        return res

# V2 
# Time:  O(n * 2^n)
# Space: O(n * 2^n)
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = [[]]
        for c in S:
            if c.isalpha():
                for i in range(len(result)):
                    result.append(result[i][:])
                    result[i].append(c.lower())
                    result[-1].append(c.upper())
            else:
                for s in result:
                    s.append(c)
        return map("".join, result)
