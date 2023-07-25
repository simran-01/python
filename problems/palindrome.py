
# palindrome


def palindrome(input_str):
    reverse = str(input_str)[::-1]
    if str(input_str).lower() == reverse.lower():
        print("palindrome")
    else:
        print("not a palindrome")


palindrome("madam")
palindrome(1001)
palindrome(100)


def al_palindrome(input_str):
    rev_str = ""
    for i in input_str:
        rev_str = i+rev_str

    if rev_str == input_str:
        print("palindrome")
    else:
        print("not a palindrome")
