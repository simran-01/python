
# vowels


def check_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    for i in text:
        if i.lower() in vowels:
            return True

    return False


print(check_vowels("fly"))

