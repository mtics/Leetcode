class Solution:
    def isValid(self, s: str) -> bool:

        chars = list(s)

        if len(chars) == 0:
            return True

        rs = list()

        rs.append(chars.pop())

        flag = False

        while len(chars) != 0:

            flag = False
            l = chars.pop()

            if len(rs) != 0:
                if rs[len(rs) - 1] == ")":
                    if l == "(":
                        rs.pop()
                        flag = True
                    else:
                        rs.append(l)

                elif rs[len(rs) - 1] == "]":
                    if l == "[":
                        rs.pop()
                        flag = True
                    else:
                        rs.append(l)

                elif rs[len(rs) - 1] == "}":
                    if l == "{":
                        rs.pop()
                        flag = True
                    else:
                        rs.append(l)
                else:
                    return False
            else:
                rs.append(l)

        if not flag:
            return False

        if len(chars) == 0 and len(rs) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()

    ss = ["", "()", "()[]{}", "(]", "([)]", "{[]}"]

    for s in ss:
        flag = solution.isValid(s)

        if flag:
            print("True")
        else:
            print("False")

    # s = "()[]{}"
    #
    # flag = solution.isValid(s)
    #
    # if flag:
    #     print("True")
    # else:
    #     print("False")
