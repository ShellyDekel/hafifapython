# 3
def removeVowels(string: str):
    return "".join([letter for letter in string if letter not in ["a", "e", "i", "o", "u"]])