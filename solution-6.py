# Maura Hurley 31 March 2019
# Solution to problem 6 in the 2019 Problem Set
# Output every second word

# Ask the user for a sentence(string) and call it s:
s = str (input("Please enter a sentence: "))

# Use the split to break up the sentence into words
# Modified from stackoverflow [https://stackoverflow.com/a/47085688]
for words in s.split()[::2]:
# Used stackoverflow to help print across [https://stackoverflow.com/a/10750004]
    print(words,end=' ')