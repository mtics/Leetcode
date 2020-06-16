class Solution:

    # 字符          数值
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        char_list = list(s)

        sum = 0

        last_char = char_list[0]

        for char in char_list:

            char_to_int = roman_dict.get(char)

            if roman_dict.get(last_char) < char_to_int:
                if ((last_char == "I") and (char == "V" or char == "X")) or \
                        ((last_char == "X") and (char == "L" or char == "C")) or \
                        ((last_char == "C") and (char == "D" or char == "M")):
                    sum = char_to_int - 2 * roman_dict.get(last_char) + sum
            else:
                sum = char_to_int + sum

            last_char = char

        return sum


if __name__ == "__main__":
    solution = Solution()

    # print(solution.romanToInt("MCMXCIV"))

    ss = ["III", "IV", "IX", "LVIII", "MCMXCIV"]

    for s in ss:
        print(solution.romanToInt(s))
