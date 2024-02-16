# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
file_ext = ""

for char in filename: 
    if char == ".":
        file_ext += char
    elif file_ext == ".":
        file_ext += char
    elif file_ext == ".p":
        file_ext += char
    elif file_ext == ".pd":
        file_ext += char

print(file_ext)

if  file_ext == ".pdf":
    print(f"{filename} is a pdf file")