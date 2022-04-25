"""
Check to see if the user is issuing "administrator" commands. I.E. /exit, /update etc.
These commands are designed to make it so updates are as easy as possible.
We are checking to see if a certain user ID is within a text file.
If so, the action can continue. If not it will fail.
"""

def is_administrator(id):
	af = open("config/admins.txt", "r")
	admins = af.read().splitlines("\n")
	af.close()
	return id in admins

