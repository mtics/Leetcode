class Solution:

    def reverse(self, x: int) -> int:
        temp = abs(x)
        final = 0

        # 若temp不为0，则对其除10
        while temp != 0:
            final = final * 10 + temp % 10
            temp = int(temp / 10)

        if 2**31 - 1 < final or final < (-2)**31:
            final = 0

        if x < 0:
            final = -final

        return final


if __name__ == "__main__":
    solution = Solution()

    print(solution.reverse(123))
