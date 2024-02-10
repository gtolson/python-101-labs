# Which of the following strings is the longest?
# Use the len() function to find out.

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

german_word_length = len(longest_german_word)
hungarian_word_length = len(longest_hungarian_word)
finnish_word_length = len(longest_finnish_word)
strong_password_length = len(strong_password)



print(f"longest_german_word is: {german_word_length}")
print(f"longest_hungarian_word is: {hungarian_word_length}")
print(f"longest_finnish_word is: {finnish_word_length}")
print(f"strong_password is: {strong_password_length}")

