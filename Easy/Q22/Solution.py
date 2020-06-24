class Solution:
    def removeDuplicates(self, nums: list) -> int:
        nums_set = list()

        index = 0

        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]

        return index+1


if __name__ == "__main__":
    solution = Solution()

    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums = [-1, 0, 0, 0, 0, 3, 3]
    print(solution.removeDuplicates(nums))
