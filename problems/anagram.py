
# anagram

def anagram(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()
    if len(text1) == len(text2):

        if sorted(text1) == sorted(text2):
            return "Anagram"

        else:
            return "Not anagram"

    else:
        return "Not anagram"


print(anagram("care", "Race"))
