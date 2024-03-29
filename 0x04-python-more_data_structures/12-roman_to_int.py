#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_di = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_num = 0
    for r in range(len(roman_string)):
        if r > 0 and roman_di[roman_string[r]] > roman_di[roman_string[r - 1]]:
            roman_num += roman_di[roman_string[r]] - 2 * \
                        roman_di[roman_string[r - 1]]
        else:
            roman_num += roman_di[roman_string[r]]
    return roman_num
