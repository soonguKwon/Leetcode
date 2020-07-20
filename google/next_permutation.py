from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_index=-1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]: last_index = i

        if last_index == -1:
            nums.reverse()
            return

        for i in range(len(nums)-1, last_index, -1):
            if nums[last_index] < nums[i]:
                nums[last_index], nums[i] = nums[i], nums[last_index]
                break

        nums[last_index+1:] = sorted(nums[last_index+1:])
        return nums


if __name__ == '__main__':
    num = [3,2,1]
    s = Solution()
    print (s.nextPermutation(num))