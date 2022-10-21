def romanToInt(numerals: str) -> int:
    numeral_to_decimal = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    numeral_string_as_integers = [
        numeral_to_decimal[numeral] for numeral in numerals[::-1]]
    numeral_as_int = 0
    while len(numeral_string_as_integers) != 0:
        if len(numeral_string_as_integers) == 1 or numeral_string_as_integers[1] >= numeral_string_as_integers[0]:
            numeral_as_int += numeral_string_as_integers[0]
            del numeral_string_as_integers[:1]
            continue
        numeral_string_as_integers[1] < numeral_string_as_integers[0]
        numeral_as_int += numeral_string_as_integers[0] - \
            numeral_string_as_integers[1]
        del numeral_string_as_integers[:2]
    return numeral_as_int


s = "III"
print(romanToInt(s))
