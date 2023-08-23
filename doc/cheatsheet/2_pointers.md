# Two pointers

- Ref
    - [fucking-algorithm : 2 pointers](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE%E8%AF%A6%E8%A7%A3.md)

## 0) Concept  

### 0-1) Types

- Pointer types
    - `Fast - Slow pointers`
        - fast, slow pointers from `same start point`
        - Usualy set
            - slow pointer moves 1 idx
            - fast pointer moves 2 idx
        - linked list
            - find mid point of linked list
            - check if linked list is circular
                - LC 141
                - LC 142
            - if a circular linked list, return beginning point of circular
            - find last k elements of a single linked list
    - `Left- Right pointers`
        - left, right pointers from `idx = 0, idx = len(n) - 1` respectively
        - Usually set
            - left pointer = 0
            - right pointer = len(nums)
        - [binary search](https://github.com/yennanliu/CS_basics/blob/master/doc/cheatsheet/binary_search.md)
        - array reverse
        - [2 sum](https://github.com/yennanliu/CS_basics/blob/master/doc/cheatsheet/n_sum.md)
        - [sliding window](https://github.com/yennanliu/CS_basics/blob/master/doc/cheatsheet/sliding_window.md)

- `Expand` from center (and Deal with `odd, even` cases)
    - LC 680
    - LC 647
    - LC 005
- Merge Sorted Array
    - LC 88

- Minimum Swaps to Group All 1's Together
    - LC 1151 (check [sliding_window.md](https://github.com/yennanliu/CS_basics/blob/master/doc/cheatsheet/sliding_window.md))

- Algorithm
    - binary search
    - sliding window
    - for loop + "expand `left`, `right` from center"

- Data structure
    - Array
    - Linked list

### 0-2) Pattern

#### 0-2-1) for loop + "expand `left`, `right` from center"
```python
# LC 005  Longest Palindromic Substring
# LC 647 Palindromic Substrings
# python
# pseudo code
# ...
for i in range(lens(s)):
    
    # if odd
    left = right = i
    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right+1-left > len(res):
            res = s[left:right+1]
        left -= 1
        right += 1
    
    # if even
    left = i - 1
    right = i
    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right+1-left > len(res):
            res = s[left:right+1]
        left -= 1
        right += 1
# ...
```

## 1) General form

### 1-1) Basic OP

#### 1-1-1 : Check if there is a circular linked list 
```java
// java
boolean hasCycle(ListNode head){
    fast = slow = head;
    // NOTE : while loop condition
    while (fast != null and fast.next != null){
        /** NOTE : need to do move slow, fast pointer then compare them */
        slow = slow.next;
        fast = fast.next.next;
        if (fast == slow){
            return True
        }
    }
    return False;
}
```

#### 1-1-2 : return the "ring start point" of circular linked list 
```java
// java
ListNode detectCycle(ListNode head){
    ListNode fast, slow;
    fast = slow = head;
    while (fast != null and fast.next != null){
        fast = fast.next.next;
        slow = slow.next;
        if (fast == slow){
            break;
        }
    }
    slow = head;
    // may need below logic to check whether is cycle linked list or not
    // if (! fast or ! fast.next){
    //     return null;
    // }
    while (slow != fast){
        slow = slow.next;
        fast = fast.next;
    }
    return slow;
}
```

```python
# LC 142. Linked List Cycle II
# python
class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        #print ("slow = " + str(slow) + " fast = " + str(fast))
        ### NOTE : via below condition check if is a cycle linked list
        if not fast or not fast.next:
            return
        """
        ### NOTE : re-init slow or fast as head (from starting point)
        -> can init slow or head
        """
        slow = head
        #fast = head 
        """
        ### NOTE : check while slow != fast
        ### NOTE : use the same speed
        """
        while slow != fast:
            # NOTE this !!! : fast, slow move SAME speed (in this step)
            fast = fast.next
            slow = slow.next
        return slow

# V0'
# IDEA : SET
class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return
        s = set()
        while head:
            s.add(head)
            head = head.next
            if head in s:
                return head
        return
```
#### 1-1-3 : find mid point of a single linked list
```java
// java
while (fast != null and fast.next != null){
    fast = fast.next.next;
    slow = slow.next;
}
return slow;
```

#### 1-1-4 : find last k elements in a single linked list
```java
// java
ListNode fast, slow;
slow = fast = head;
while (k > 0){
    fast = fast.next;
    k -= 1;
}
while (fast != null){
    fast = fast.next;
    slow = slow.next;
}
return slow;
```

#### 1-1-5 : Reverse Array
```java
// java
void reverse(int[] nums){
    int left = 0;
    int right = nums.length - 1
    while (left < right){
        int tmp = nums(left);
        nums(left) = nums(right)
        nums(right) = tmp;
        left += 1;
        right -= 1;
    }
}
```

#### 1-1-6: [binary search](https://github.com/yennanliu/CS_basics/blob/master/doc/cheatsheet/binary_search.md)

#### 1-1-7: [sliding window](https://github.com/yennanliu/CS_basics/blob/master/doc/cheatsheet/sliding_window.md)


## 2) LC Example

### 2-1) Remove Element
```python
# python
# basic
class Solution(object):
    def removeElement(self, nums, val):
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length
```

```python
# LC 026 : Remove Duplicates from Sorted Array
# https://github.com/yennanliu/CS_basics/blob/master/leetcode_python/Array/remove-duplicates-from-sorted-array.py
# V0
# IDEA : 2 POINTERS: i, j
class Solution(object):
    def removeDuplicates(self, nums):
        # edge case
        if not nums:
            return
        i = 0
        for j in range(1, len(nums)):
            """
            NOTE !!!
             -> note this condition
             -> we HAVE to swap i+1, j once nums[i], nums[j] are different
             -> so we MAKE SURE there is no duplicate
            """
            if nums[j] != nums[i]:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1

        #print ("nums = " + str(nums))
        return i+1

# V0'
# IDEA : 2 POINTERS
# HAVE A POINTER j STARTS FROM 0 AND THE OTHER POINTER i GO THROUGH nums
#  -> IF A[i] != A[j]
#     -> THEN SWITCH A[i] AND A[j+1]
#     -> and j += 1
# *** NOTE : it's swith A[j+1] (j+1) with A[i]
# DEMO 1 
# A = [1,1,1,2,3]
# s = Solution()
# s.removeDuplicates(A)
# [1, 1, 1, 2, 3]
# [1, 1, 1, 2, 3]
# [1, 1, 1, 2, 3]
# [1, 2, 1, 1, 3]
# [1, 2, 3, 1, 1]
#
# DEMO 2
# A = [1,2,2,3,4]
# s = Solution()
# s.removeDuplicates(A)
# A = [1, 2, 2, 3, 4]
# A = [1, 2, 2, 3, 4]
# A = [1, 2, 2, 3, 4]
# A = [1, 2, 2, 3, 4]
# A = [1, 2, 3, 2, 4]
# -> A = [1, 2, 3, 4, 2]
class Solution:
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        j = 0
        for i in range(0, len(A)):
            ###  NOTE : below condition
            if A[i] != A[j]:
                A[i], A[j+1] = A[j+1], A[i]
                j = j + 1
        return j+1
```

```python
# LC 283 move-zeroes
# V0
class Solution(object):
    def moveZeroes(self, nums):
        y = 0
        for x in range(len(nums)):
            if nums[x] != 0:
                nums[x], nums[y] = nums[y], nums[x]
                y += 1
        return nums

# V0'
class Solution(object):
    def moveZeroes(self, nums):
        # edge case
        if not nums:
            return
        j = 0
        for i in range(1, len(nums)):
            # if nums[j] = 0, swap with nums[i]
            if nums[j] == 0:
                if nums[i] != 0:
                    nums[j], nums[i] = nums[i], nums[j]
                    j += 1
            # if nums[j] != 0, then move j (j+=1) for searching next 0
            else:
                j += 1
        return nums
```

```python
# LC 080 : Remove Duplicates from Sorted Array II
# V0
# IDEA : 2 POINTERS
#### NOTE : THE nums already ordering
# DEMO
# example 1
# nums = [1,1,1,2,2,3]
#           i j
#           i   j
#        [1,1,2,1,2,3]
#             i   j
#        [1,1,2,2,1,3]
#               i   j
#
# example 2
# nums = [0,0,1,1,1,1,2,3,3] 
#           i j
#        [0,0,1,1,1,1,2,3,3]
#             i j
#        [0,0,1,1,1,1,2,3,3]
#               i j
#        [0,0,1,1,1,1,2,3,3]
#               i   j
#               i     j
#        [0,0,1,1,2,1,1,3,3]
#                 i     j  
#        [0,0,1,1,2,3,1,1,3]
#                   i     j
#        [0,0,1,1,2,3,3,1,1]
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 3:
            return len(nums)

        ### NOTE : slow starts from 1
        slow = 1
        ### NOTE : fast starts from 2
        for fast in range(2, len(nums)):
            """
            NOTE : BELOW CONDITION

            1) nums[slow] != nums[fast]: for adding "1st" element
            2) nums[slow] != nums[slow-1] : for adding "2nd" element
            """
            if nums[slow] != nums[fast] or nums[slow] != nums[slow-1]:
                # both of below op are OK
                #nums[slow+1] = nums[fast]
                nums[slow+1], nums[fast] = nums[fast], nums[slow+1] 
                slow += 1
        return slow+1
```

### 2-2) Longest Palindromic Substring
```python
# LC 005 Longest Palindromic Substring
# V0
# IDEA : TWO POINTERS
# -> DEAL WITH odd, even len cases
#  -> step 1) for loop on idx 
#  -> step 2) and start from "center" 
#  -> step 3) and do a while loop
#  -> step 4) check if len of sub str > 1
# https://leetcode.com/problems/longest-palindromic-substring/discuss/1025355/Easy-to-understand-solution-with-O(n2)-time-complexity
# Time complexity = best case O(n) to worse case O(n^2)
# Space complexity = O(1) if not considering the space complexity for result, as all the comparison happens in place.
class Solution:
    # The logic I have used is very simple, iterate over each character in the array and assming that its the center of a palindrome step in either direction to see how far you can go by keeping the property of palindrome true. The trick is that the palindrome can be of odd or even length and in each case the center will be different.
    # For odd length palindrome i am considering the index being iterating on is the center, thereby also catching the scenario of a palindrome with a length of 1.
    # For even length palindrome I am considering the index being iterating over and the next element on the left is the center.
    def longestPalindrome(self, s):

        if len(s) <= 1:
            return s

        res = []

        for idx in range(len(s)):
        
            """
            # CASE 1) : odd len
            # Check for odd length palindrome with idx at its center

            -> NOTE : the only difference (between odd, even len)
            
            -> NOTE !!!  : 2 idx : left = right = idx
            """
            left = right = idx
            # note the condition !!!
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(res):
                    res = s[left:right + 1]
                left -= 1
                right += 1
              
            """"
            # CASE 2) : even len  
            # Check for even length palindrome with idx and idx-1 as its center

            -> NOTE : the only difference (between odd, even len)

            -> NOTE !!!  : 2 idx : left = idx - 1,  right = idx
            """
            left = idx - 1
            right = idx
            # note the condition !!!
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(res):
                    res = s[left:right + 1]
                left -= 1
                right += 1

        return res

# V0'
# IDEA : TWO POINTER + RECURSION
# https://leetcode.com/problems/longest-palindromic-substring/discuss/1057629/Python.-Super-simple-and-easy-understanding-solution.-O(n2).
class Solution:
    def longestPalindrome(self, s):
        res = ""
        length = len(s)
        def helper(left, right):
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1      
            return s[left + 1 : right]
        
        for index in range(len(s)):
            res = max(helper(index, index), helper(index, index + 1), res, key = len)           
        return res
```

### 2-3) Container With Most Water
```python
# LC 11 Container With Most Water
# V0 
# IDEA : TWO POINTERS 
class Solution(object):
    def maxArea(self, height):
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
```

### 2-4) Longest Consecutive Sequence
```python
# LC 128 Longest Consecutive Sequence

# V0
# IDEA : sliding window
class Solution(object):
    def longestConsecutive(self, nums):
        # edge case
        if not nums:
            return 0
        nums = list(set(nums))
        # if len(nums) == 1: # not necessary
        #     return 1
        # sort first
        nums.sort()
        res = 0
        l = 0
        r = 1
        """
        NOTE !!!

        Sliding window here :
            condition :  l, r are still in list (r < len(nums) and l < len(nums))

            2 cases

                case 1) nums[r] != nums[r-1] + 1
                    -> means not continous, 
                        -> so we need to move r to right (1 idx)
                        -> and MOVE l to r - 1, since it's NOT possible to have any continous subarray within [l, r] anymore
                case 2) nums[r] == nums[r-1] + 1
                        -> means there is continous subarray currently, so we keep moving r to right (r+=1) and get current max sub array length (res = max(res, r-l+1))
        """
        while r < len(nums) and l < len(nums):
            # case 1)
            if nums[r] != nums[r-1] + 1:
                r += 1
                l = (r-1)
            # case 2)
            else:
                res = max(res, r-l+1)
                r += 1
        # edge case : if res == 0, means no continous array (with len > 1), so we return 1 (a single alphabet can be recognized as a "continous assay", and its len = 1)
        return res if res > 1 else 1

# V0'
# IDEA : SORTING + 2 POINTERS
class Solution(object):
    def longestConsecutive(self, nums):
        # edge case
        if not nums:
            return 0

        nums.sort()
        cur_len = 1
        max_len = 1
        #print ("nums = " + str(nums))

        # NOTE : start from idx = 1
        for i in range(1, len(nums)):
            ### NOTE : start from nums[i] != nums[i-1] case
            if nums[i] != nums[i-1]:
                ### NOTE : if nums[i] == nums[i-1]+1 : cur_len += 1
                if nums[i] == nums[i-1]+1:
                    cur_len += 1
                ### NOTE : if nums[i] != nums[i-1]+1 : get max len, and reset cur_lent as 1
                else:
                    max_len = max(max_len, cur_len)
                    cur_len = 1
        # check max len again
        return max(max_len, cur_len)
```

### 2-6) Palindromic Substrings
```python
# LC 647. Palindromic Substrings
# V0'
# IDEA : TWO POINTERS
# https://leetcode.com/problems/palindromic-substrings/discuss/1041760/Python-Easy-Solution-Beats-85
# https://github.com/yennanliu/CS_basics/blob/master/leetcode_python/String/longest-palindromic-substring.py
class Solution:
    def countSubstrings(self, s):
        ans = 0    
        for i in range(len(s)):
            # odd
            ans += self.helper(s, i, i)
            # even
            ans += self.helper(s, i, i + 1)  
        return ans
        
    def helper(self, s, l, r):     
        ans = 0    
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            ans += 1          
        return ans

# V0
# IDEA : BRUTE FORCE
class Solution(object):
    def countSubstrings(self, s):
        count = 0
        # NOTE: since i from 0 to len(s) - 1, so for j we need to "+1" then can get go throgh all elements in str
        for i in range(len(s)):
            # Note : for j we need to "+1"
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    count += 1
        return count

# V0''
# IDEA : TWO POINTERS (similar as LC 005)
class Solution(object):
    def countSubstrings(self, s):
        count = 0
        for i in range(len(s)):
            # for every single character
            count += 1
            
            # case 1) palindromic substrings length is odd 
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            # case 2) palindromic substrings length is even 
            left = i - 1
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count
```

### 2-7) Sum of Subarray Ranges
```python
# LC 2104. Sum of Subarray Ranges
# V0
# IDEA : BRUTE FORCE
class Solution:
    def subArrayRanges(self, nums):
        res = 0
        for i in range(len(nums)):
            curMin = float("inf")
            curMax = -float("inf")
            for j in range(i, len(nums)):
                curMin = min(curMin, nums[j])
                curMax = max(curMax, nums[j])
                res += curMax - curMin
        return res

# V0'
# IDEA : INCREASING STACK
class Solution:
    def subArrayRanges(self, A0):
        res = 0
        inf = float('inf')
        A = [-inf] + A0 + [-inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res -= A[j] * (i - j) * (j - k)
            s.append(i)
            
        A = [inf] + A0 + [inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] < x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res
```

### 2-8) Trapping Rain Water
```python
# LC 42. Trapping Rain Water
# NOTE : there is also 2 scan, dp approaches
# V0'
# IDEA : TWO POINTERS 
# IDEA : CORE
#     -> step 1) use left_max, right_mex : record "highest" "wall" in left, right handside at current idx
#     -> step 2) 
#                case 2-1) if height[left] < height[right] : 
#                   -> all left passed idx's height is LOWER than height[right]
#                   -> so the "short" wall MUST on left
#                   -> and since we record left_max, so we can get trap amount based on left_max, height[left]
#                
#                case 2-2) if height[left] > height[right]
#                   -> .... (similar as above)
class Solution:
    def trap(self, height):
 
        if not height:
            return 0

        left_max = right_max = res = 0
        left, right = 0, len(height) - 1
 
        while left < right:
            if height[left] < height[right]:  # left pointer op
                if height[left] < left_max:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1  # move left pointer 
            else:
                if height[right] < right_max:  # right pointer op
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1  # move right pointer 
        return res
```

### 2-9) Next Permutation
```python
# LC 31. Next Permutation
# V0
class Solution:
    def nextPermutation(self, nums):
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return 
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -= 1

# V0'
class Solution(object):
    def nextPermutation(self, num):
        k, l = -1, 0
        for i in range(len(num) - 1):
            if num[i] < num[i + 1]:
                k = i

        if k == -1:
            num.reverse()
            return

        for i in range(k + 1, len(num)):
            if num[i] > num[k]:
                l = i
        num[k], num[l] = num[l], num[k]
        num[k + 1:] = num[:k:-1] ### dounle check here ###
```

### 2-10) Valid Palindrome II
```python
# LC 680. Valid Palindrome II
class Solution:
    def validPalindrome(self, s):
        
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                """
                # NOTE this !!!!
                -> break down the problem to even, odd cases
                """
                even, odd = s[l:r], s[l+1:r+1]
                # NOTE this !!!!
                return even == even[::-1] or odd == odd[::-1]
            else:
                l += 1
                r -= 1
                
        return True 
```

### 2-11) Merge Sorted Array
```python
# LC 88. Merge Sorted Array
# V0
# IDEA : 2 pointers
### NOTE : we need to merge the sorted arrat to nums1 with IN PLACE (CAN'T USE EXTRA CACHE)
# -> SO WE START FROM RIGHT HAND SIDE (biggeest element) to LEFT HAND SIDE (smallest element)
# -> Then paste the remain elements
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ### NOTE : we define 2 pointers (p, q) here
        p, q = m-1, n-1
        ### NOTE : the while loop conditions
        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                #***** NOTE : WE START FROM p+q+1 index, since that's the count of non-zero elements in nums1, and nums2
                nums1[p+q+1] = nums1[p]
                p = p-1
            else:
                ### NOTE WE START FROM p+q+1 index, reason same as above
                nums1[p+q+1] = nums2[q]
                q = q-1
        # if there're still elements in nums2, we just replace the ones in nums1[:q+1] with them (nums2[:q+1])
        nums1[:q+1] = nums2[:q+1]
```