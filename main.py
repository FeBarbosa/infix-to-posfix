from regex import regex

rgx = regex("x+y+(5z)*+2")
if rgx.isValid():
    print("Everything Ok!!!")
else:
    print("invalid expression! :(")