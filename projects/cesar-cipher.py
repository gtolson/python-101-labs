#!/usr/bin/python

#####
# Global vars
#####
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punc_chars = [" ", ",", ".", "!", "?", "$", ":", ";", "'"]
#secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 12
chars = []
dchars = []
encrypt_chars = ""
decrypt_chars = ""

secret = input("Please enter the string you want to encrypt: ")

#####
# Encrypt
#####
for char in secret:
    if char in lowercase_letters:
        char_index = lowercase_letters.find(char)
        if char_index <= (25 - cipher):
            chars.append(lowercase_letters[char_index + cipher])
        elif char_index >= (25 - cipher + 1):
            chars.append(lowercase_letters[cipher - (26 - char_index)])
    if char in uppercase_letters:
        char_index = uppercase_letters.find(char)
        if char_index <= (25 - cipher):
            chars.append(uppercase_letters[char_index + cipher])
        elif char_index >= (25 - cipher + 1):
            chars.append(uppercase_letters[cipher - (26 - char_index)])
        elif char == "":
            chars.append(char)
    for punc in punc_chars:
        if char == punc:
            chars.append(punc)

for i in chars:
    encrypt_chars += str(i)
print(encrypt_chars)

######
# Decrypt
#####

for dchar in encrypt_chars:
    if dchar in lowercase_letters:
        dchar_index = lowercase_letters.find(dchar)
        if dchar_index >= (0 + cipher):
            dchars.append(lowercase_letters[dchar_index - cipher])
        elif dchar_index <= (0 + cipher + 1):
            dchars.append(lowercase_letters[26 - (cipher - dchar_index )])
    if dchar in uppercase_letters:
        dchar_index = uppercase_letters.find(dchar)
        if dchar_index >= (0 + cipher):
            dchars.append(uppercase_letters[dchar_index - cipher])
        elif dchar_index <= (0 + cipher + 1):
            dchars.append(lowercase_letters[26 - (cipher - dchar_index )])
    for punc in punc_chars:
        if dchar == punc:
            dchars.append(punc)

for i in dchars:
    decrypt_chars += str(i)
print(decrypt_chars)