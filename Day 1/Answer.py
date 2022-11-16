x = input()
list = ['A','E','I','O','U','a','e','i','o','u']
if x in list:
    print("Vowel")
elif not x.isalpha():
    print("Invalid Input")
else:
    print("Consonant")
