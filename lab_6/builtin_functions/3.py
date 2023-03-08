#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
string = input()

pol = "".join(reversed(string))

if string == pol:
    print("Polindrome string :)")
else:
    print("Not Polindrome string :(")