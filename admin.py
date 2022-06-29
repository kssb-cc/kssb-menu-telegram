"""
Check to see if the user is issuing "administrator" commands. I.E. /exit, /update etc.
"""


def is_administrator(id):
    id = str(id)
    admins = []
    with open("config/admins.txt", "r") as f:
        admins = f.read().splitlines()
    return id in admins
