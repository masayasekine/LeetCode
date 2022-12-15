from typing import Dict


class Solution:
    def romanToInt(self, s: str) -> int:
        normal: Dict[str, str] = {
            "I": "1",
            "v": "4",
            "V": "5",
            "x": "9",
            "X": "10",
            "l": "40",
            "L": "50",
            "c": "90",
            "C": "100",
            "d": "400",
            "D": "500",
            "m": "900",
            "M": "1000",
        }
        con_normal = str.maketrans(normal)
        s2 = (
            s.replace("IV", "v")
            .replace("IX", "x")
            .replace("XL", "l")
            .replace("XC", "c")
            .replace("CD", "d")
            .replace("CM", "m")
        )
        s2_list = list(s2)
        num_list = [int(n.translate(con_normal)) for n in s2_list]
        return sum(num_list)


if __name__ == "__main__":
    Solution().romanToInt("MCMXCIV")
