def check_palindrome(txt):
    txt = txt.upper()
    if txt[::-1] == txt:
        return True
    return False

txt = input("Introduce a word, number or char to check if it's palindrome: ")

print(f"the result of this operation is {check_palindrome(txt)}")