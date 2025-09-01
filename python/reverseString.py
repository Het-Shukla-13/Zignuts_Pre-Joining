def reverseString(str):
    revStr=""
    for i in str:
        revStr=i+revStr
    return revStr

inputStr=input("Enter a string: ")
print(f"Reversed string: {reverseString(inputStr)}")