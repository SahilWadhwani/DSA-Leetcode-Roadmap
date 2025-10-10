"""
LeetCode: 71. Simplify Path  
Difficulty: Medium  
Link: https://leetcode.com/problems/simplify-path/

Approach:
---------
This problem requires simplifying a given Unix-style absolute path.
We break the path into components using `/` as a separator, and simulate
a stack-based navigation as follows:

1. Ignore empty strings and '.' (current directory).
2. For '..' (parent directory), we pop from the stack if it's not empty.
3. For valid directory names, we push them onto the stack.
4. At the end, we rebuild the canonical path by joining stack components with '/'.

Example:  
Input: "/a/./b/../../c/"  
→ Components: ['a', '.', 'b', '..', '..', 'c']  
→ Stack after processing: ['c']  
→ Output: "/c"

Time Complexity: O(n)  
Space Complexity: O(n)  
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "." or part == "":
                continue  # Skip current directory or redundant slashes
            elif part == "..":
                if stack:
                    stack.pop()  # Go up one level if possible
            else:
                stack.append(part)  # Valid directory name

        return "/" + "/".join(stack)  # Construct the canonical path
