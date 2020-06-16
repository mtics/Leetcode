class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = list(str(x))

        index = len(temp)

        for ch in temp:
            index -= 1
            if ch != temp[index]:
                return False

        return True


if __name__=="__main__":

    solution = Solution()

    print(solution.isPalindrome(-121))
