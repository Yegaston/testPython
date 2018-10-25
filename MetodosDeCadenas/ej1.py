
email = input("Introduce tu email: ")

arrobas = email.count('@')
if(arrobas != 1 or email.rfind('@')==(len(email)-1)):
    print("Wrong mail")
else:
    print("Correct")