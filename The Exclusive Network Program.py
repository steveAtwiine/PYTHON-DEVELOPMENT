#The Exclusive Network Progrmme
#This program accepts you Log-in information basing on the surname 
# or password you have used to Log-in into the system...

print("\t\tTHE EXECUTIVE CLUB LOG-IN PROGRAMME")
print("\n")
print("\t\tProvide your password to proceed") 
print("\n")
print("\t\t\tMembers Only !")

#Username
username = ""
while not username:
    username = input("Username: ")

#Password
password = ""
while not password:
    password = input("Password: ")

if username == "steve" and password == "steve100":
    print("You\'re Welcome",username)
elif username == "simon" and password == "simon100":
    print("Hello",username)
elif username == "victor"  or password == "viitoHP":
    print("Hello Sir...!",)
elif username == "guest" or password == "guest":
    print("Hello",username)
else:
    print("You\'re not a member of the Executive")