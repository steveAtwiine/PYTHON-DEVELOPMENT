#A Password Program
#This programallows access to an individual
#who gets or types in the right password.

print("\t\t\tHello there, Welcome to the Access Point Password Program")
print ("\n\t\t\t--You\'ll only be granted Access if you use the right password--")

password = input("\n\t\t\tPlease type in your password...")

if password == "Stephen":
    print("\n\t\t\tHello " + password, "Access Granted")
else:
    print("\n\t\t\tPlease try somewhere else...")