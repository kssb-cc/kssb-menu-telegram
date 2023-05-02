def is_administrator(id):
	id = str(id)
	admins = []
	with open("config/admins.txt", "r") as f:
		admins = f.read().splitlines()
	return id in admins
