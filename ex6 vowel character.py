str = input("Enter the string: ")
newStr = ""
for ch in str : 
    letter = ch.lower()
    if letter == 'a' \
       or letter == 'e' \
       or letter == 'i' \
       or letter == 'o' \
       or letter == 'u' :
        newStr += '@'
    else :
        newStr += ch
print(newStr)
