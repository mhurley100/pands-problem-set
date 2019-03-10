# Maura Hurley 31 March 2019
# Solution to problem 6 in the 2019 Problem Set
# Output every second word

# Ask the user for a sentence(string) and call it s:

s = str (input("Please enter a sentence: "))
for words in s.split()[::2]:
    print(words)