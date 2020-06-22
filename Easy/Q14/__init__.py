class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        for i, L in enumerate((*(len(set(t)) for t in zip(*strs)), 2)):
            if L > 1:
                return (*strs, "")[0][:i]

    # def longestCommonPrefix(self, strs: list) -> str:
    #
    #     chars_list = list()
    #
    #     for string in strs:
    #         chars_list.append(list(string))
    #
    #     length = 65535
    #
    #     for chars in chars_list:
    #         if length > len(chars):
    #             length = len(chars)
    #
    #     prefix = ""
    #     temp = ""
    #     flag = True
    #
    #     for i in range(length):
    #         for j in range(len(chars_list)):
    #             if j == 0:
    #                 temp = chars_list[j][i]
    #             else:
    #                 if temp != chars_list[j][i]:
    #                     flag = False
    #
    #         if flag:
    #             prefix += temp
    #         else:
    #             break
    #
    #     return prefix


if __name__ == "__main__":
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    print(solution.longestCommonPrefix(strs))
