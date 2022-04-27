"""
Check to see if the user is issuing "administrator" commands. I.E. /exit, /update etc.
These commands are designed to make it so updates are as easy as possible.
We are checking to see if a certain user ID is within a text file.
If so, the action can continue. If not it will fail.
"""

def is_administrator(id):
	id = str(id)
	admins = []
	print("Type of ID: "+str(type(id)))
	with open("config/admins.txt", "r") as f:
		admins = f.read().splitlines()
	print("Okay. "+str(admins))
	print(str(id in admins))
	return id in admins
