from collections import deque

# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limi

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # O(n) sliding window approach with two monotonic deques.
        # It is O(n) because we only ever push/pop an element once into the deques.
        # We use two monotonic deques because we want to keep track of the
        # min and max of our sliding window since that information is all
        # that is needed to calculate whether the limit is satisfied.
        # The monotonic property allows us to efficiently adjust the
        # left bound of the window.

        # we will maintain a monotonic deque for both max and min values
        # containing the value and the index of the value
        min_dq = deque()
        max_dq = deque()

        # start is the index of the start of the current sliding window
        start = 0
        max_len = 0

        for i in range(len(nums)):
            # the only times we need to adjust start is if the difference between
            # our new element and the prev max/min in window exceeds limit.
            # when that happens, the start index of window must be adjusted

            while min_dq and abs(nums[i] - min_dq[0][0]) > limit:
                start = min_dq.popleft()[1] + 1

            while max_dq and abs(nums[i] - max_dq[0][0]) > limit:
                # take the max of the start value because
                # we want the narrowest valid range for new window
                # and the start when popping off min_dq above might have been later
                start = max(start, max_dq.popleft()[1] + 1)

            # insert the element into the monotonic deques.
            # inclusive comparisons (>=, <=) because we only care about
            # the latest index of the given value when narrowing the bounds.
            while min_dq and min_dq[-1][0] >= nums[i]:
                min_dq.pop()
            min_dq.append([nums[i], i])

            while max_dq and max_dq[-1][0] <= nums[i]:
                max_dq.pop()
            max_dq.append([nums[i], i])

            # calculate and compare new length of window containing element i
            max_len = max(max_len, i - start + 1)

        return max_len