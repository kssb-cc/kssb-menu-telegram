import requests
from bs4 import BeautifulSoup

class kssb_menu():
	def __init__(self):
		self.url = "https://kssb.net/parents/menus/"
		self.session = requests.session()
	
	def download(self):
		r = self.session.get(self.url)
		soup = BeautifulSoup(r.text, features="html.parser")
		days = []
		menus = []
		menu = {}
		for t in soup.find_all("div", class_="vc-hoverbox-front-inner"):
			days.append(t.text[1:-1])
		for tag in soup.find_all("div", class_="vc-hoverbox-back-inner"):
			temp = []
			for p in tag.find_all("p"):
				temp.append(p.text)
			menus.append('\n'.join(temp))
		
		for i in range(len(days)):
			menu[days[i]] = menus[i]
		
		return menu