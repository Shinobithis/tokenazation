import re

my_string = "Let's write RegEx! This is step 1. Next is step 2... And step 3? Finally, we have 456 words."

sentence_ending = r"[.?!]"
print(re.split(sentence_ending, my_string))

capitalized = r"[A-Z]\w+"
print(re.findall(capitalized, my_string))

spaces = r"\s+"
print(re.split(spaces, my_string))

degits = r"\d+"
print(re.findall(degits, my_string))