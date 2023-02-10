def compressed (word):
  letter_dict = {}
  for letter in word:
    if letter not in letter_dict:
      letter_dict[letter] = 1
    else:
      letter_dict[letter] = letter_dict[letter]+1
  return letter_dict

print(compressed("Hello World"))
print(compressed("Bismillah"))