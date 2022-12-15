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
        special: Dict[str, str] = {
            "IV": "v",
            "IX": "x",
            "XL": "l",
            "XC": "c",
            "CD": "d",
            "CM": "m",
        }
        con_normal = str.maketrans(normal)
        s2 = "".join(special.get(c, c) for c in s)
        s2_list = list(s2)
        num_list = [int(n.translate(con_normal)) for n in s2_list]
        print(sum(num_list))
        return sum(num_list)


if "__name__" == "__main__":
    Solution().romanToInt("III")
