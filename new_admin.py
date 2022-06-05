from sys import exit
new_admin = input("New admin? ")
if new_admin=="": exxit("Cannot be empty.")
f = open("config/admins.txt", "a")
f.write(new_admin+"\n")
f.close()
print("Okay.")
