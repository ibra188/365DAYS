"""
Caesar cipher. Specifically, you will take each letter in your message, find its position in the alphabet, take the letter located after 3 positions in the alphabet, and replace the original letter with the new letter.
"""
wariors = "Hello Worriors"
shift  = 3
new_word = "abcdefghijklmnopqrstuvwxyz"
index = new_word.find(wariors[0])
print(index) # is going to print -1 because the letters in new word are in lower case so the [0] is at index H.
index = new_word.find(wariors[0].lower())
# the if statement making so that the information is wel clear.
if index == -1:
    print("Character not found!")
else:
    print("Character found at index:", index)


# so in other to fix this, you can convert the letter to lowercase before using the find method.
index =  new_word.find(wariors[0].lower())
print(index)
shifted_index = new_word[index] # instead of printing the index value of the string which is 7 now is passing the actual letter.
print(shifted_index)

#for statement to loop through the word.
encrypted_text = '' # the encrypted text is an empty string.
for char in wariors.lower(): #the lower method is used to convert the word to lowercase.
    index = new_word.find(char) # the find method is used to find the index of the letter in the new word.
    #print(char, index) # the print statement is used to print the letter and the index of the letter in the new word.
    new_index = index + shift # the new index is the index of the letter in the new word plus the shift value.
    new_char = new_word[new_index] # the new char is the new index of the letter in the new word.
    print("Char:", char, "new_char:", new_char) # the print statement is used to print the new char.