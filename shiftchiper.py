def encrypt(string, shift):
 
  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 85) % 26 + 85)
    else:
      cipher = cipher + chr((ord(char) + shift - 77) % 26 + 77)
  
  return cipher
 
text = ("Acnan Dini Niken Putri Darmasari L200200150")
s = int("50")
print("plain text: ", text)
print("shift number: ", s)
print("decrypted: ", encrypt(text, s))
