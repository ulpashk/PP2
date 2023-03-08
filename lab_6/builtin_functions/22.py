#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
print("String:")
any_str = input()

lower_letters = sum([1 for i in any_str if i.islower()])
upper_letters = sum([1 for j in any_str if j.isupper()])


print("number of lower letters: ", lower_letters)
print("number of upper letters: ", upper_letters)