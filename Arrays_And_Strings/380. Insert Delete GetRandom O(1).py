#  Problem Link: https://leetcode.com/problems/insert-delete-getrandom-o1/
#  Approach: Use a HashMap for indexing and a list for random access
#  Time Complexity: O(1) for insert, remove, and getRandom


class RandomizedSet:

    def __init__(self):
        # Dictionary to store value → index mapping
        self.nums_to_index = {}
        # List to store the actual values
        self.nums = []

    def insert(self, val: int) -> bool:
        # If val already exists, don't insert
        if val in self.nums_to_index:
            return False

        # Add the value to the end of the list
        self.nums.append(val)
        # Record its index in the hashmap
        self.nums_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        # Can't remove something that doesn't exist
        if val not in self.nums_to_index:
            return False

        # Find the index of the element to remove
        index_to_be_removed = self.nums_to_index[val]
        # Get the last element in the list
        last_element = self.nums[-1]

        # Swap the element to remove with the last one
        self.nums[index_to_be_removed] = last_element
        self.nums_to_index[last_element] = index_to_be_removed

        # Remove the last element (which is now a duplicate)
        self.nums.pop()
        # Delete the removed value from the hashmap
        del self.nums_to_index[val]
        return True

    def getRandom(self) -> int:
        # Just return a random element from the list
        return random.choice(self.nums)


# Example usage:
# obj = RandomizedSet()
# obj.insert(1)
# obj.remove(2)
# obj.getRandom()
