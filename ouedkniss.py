import re
import requests
import os
import time
from bs4 import BeautifulSoup

from tools import *
from easySqlite3 import Db
######################################################################
######################################################################
# the search link, without the page token.
SEARCH_LINK = "https://www.ouedkniss.com/annonces/?c={}&wilaya=%2C{}"

# the search link, with the page token.
SEARCH_LINK_PAGE = "https://www.ouedkniss.com/annonces/?c={}&wilaya=%2C{}&p={}"

# The wilaya's(means states, thats how we name it in Algeria)
wilaya = [
	"Adrar", "Chlef", "Laghouat", "Oum El Bouaghi", "Batna", "Bejaia", "Biskra",
	"Béchar", "Blida", "Bouira", "Tamanrasset", "Tébessa", "Tlemcen", "Tiaret",
    "Tizi Ouzou", "Alger", "Djelfa", "Jijel", "Sétif", "Saïda", "Skikda",
    "Sidi Bel Abbes", "Annaba", "Guelma", "Constantine", "Medea", "Mostaganem", "M'Sila",
    "Mascara", "Ouargla", "Oran", "El Bayadh", "Illizi", "Bordj Bou Arreridj", "Boumerdes",
    "El Taref", "Tindouf", "Tissemsilt", "El Oued", "Khenchela", "Souk Ahras", "Tipaza",
	"Mila", "Aïn Defla", "Naama", "Aïn Temouchent", "Ghardaia", "Relizane"]

# The wilaya's(means states, that is how we name it in Algeria)
# this form supports
wilayaSearch = [
	"Adrar", "Chlef", "Laghouat", "Oum+El+Bouaghi", "Batna", "Bejaia", "Biskra",
	"Bechar", "Blida", "Bouira", "Tamanrasset", "Tebessa", "Tlemcen", "Tiaret",
    "Tizi+Ouzou", "Alger", "Djelfa", "Jijel", "Setif", "Saida", "Skikda",
    "Sidi+Bel+Abbes", "Annaba", "Guelma", "Constantine", "Medea", "Mostaganem", "MSila",
    "Mascara", "Ouargla", "Oran", "El+Bayadh", "Illizi", "Bordj+Bou+Arreridj", "Boumerdes",
    "El+Taref", "Tindouf", "Tissemsilt", "El+Oued", "Khenchela", "Souk+Ahras", "Tipaza",
	"Mila", "Ain+Defla", "Naama", "Ain+Temouchent", "Ghardaia", "Relizane"]


# the categories
# "materiaux_equipement", "voyage", "services", "boutiques"
category = [
	"telephones", "automobiles", "immobilier", "electronique",
	"informatique", "vetements", "maison", "loisirs_divertissements",
	"divers", "materiaux_equipement", "voyages", "services"
]
######################################################################
######################################################################
def getImgLink(page_link):
	"""
	To extract the link that directs us to the
	phone number's image, so we can download it
	later, and extract the phone number from it.
	:param page_link:
	:return:
	"""
	html = requests.get(str(page_link), stream=True)
	html = BeautifulSoup(html.text, 'html.parser')
	
	phone_link = html.find_all("img", alt="phone")
	phone_link = re.findall(r'//(.*\.jpg)', str(phone_link))
	
	if len(phone_link) != 0:
		phone_link = phone_link[0]
		return "https://" + str(phone_link)
	
	else:
		return ""
	
	
def getLinks(link):
	"""
	To extract the links that directs us to the
	the pages, so we can download the images that
	contains the phone numbers.
	:param link:
	:return:
	"""
	html = requests.get(link)
	html = BeautifulSoup(html.text, 'html.parser')
	
	a_link = html.find_all("li", class_="annonce_titre")
	
	for go in re.findall(r'href="(.*)" it', str(a_link)):
		yield "https://ouedkniss.com/" + go
######################################################################
######################################################################
def fetch(cat, wl, skip=-1):
	counter = 0

	# init the process
	page_counter = 1
	out = False
	
	while out is False:
		# make the search link
		link = SEARCH_LINK_PAGE.format(cat, wl, page_counter)
	
		# the links
		links = list(getLinks(link))
		# in this case the page is not valid
		# so we go to next wilaya
		if len(links) != 0:
			try:
				for an_link in links:
					if counter <= skip:
						print(counter, "Page::", page_counter)
						counter += 1
						continue
					# get the image link
					img_link = getImgLink(an_link)
						
					# if the link exists, download the image
					if len(img_link) != 0:

						# download the image
						downloadImg(img_link, "cache/" + cat + "/" +
						            str(wilayaSearch.index(wl) + 1)+"/phone" + str(counter))

						print(counter, "Page::", page_counter, "Wilaya::", wl, "Category::", cat)
						counter += 1
					else:
						continue
			except Exception as e:
				#raise e
				pass
		else:
			out = True
			continue
				
		# access the next page
		page_counter += 1


def scritch():
	file = open("/home/fares/Desktop/data_.txt", 'a')
	
	for cat in category:
	 	for wl in range(16, 17):
	 		current_dir = "/home/fares/Music/phones/cache/" + cat + "/" + str(wl) + "/"
	 		l = os.listdir(current_dir)
	 		os.chdir(current_dir)

	 		for number in l:
			 	try:
			 		numbers = imgToText(number)
			 		if numbers != "":
				 		numbers = numbers.split("/")

				 		for single in numbers:
				 			if len(single) > 1:
				 				for num in single.split("\n"):
				 					num = num.replace(" ", "")
				 					num = uniTel(num, "213")
				 					
				 					print("["+'"'+cat+'"'+","+'"'+wilaya[wl-1]+'"'+","+'"'+num+'"'+"]")
			 						
			 						file.write("["+'"'+cat+'"'+","+'"'+wilaya[wl-1]+'"'+","+'"'+num+'"'+"]")
			 						file.write("\n")
			 	except Exception as e:
			 		pass

	file.close()

def write_to_base():
	query = " INSERT INTO phone(number,category,wilaya) VALUES(?,?,?)"
	db = Db("dataAr/data.db")

	print("DATA BASE OPENED:: ", db.connect())
	print("QUERY PREPARED:: ", db.prepareQuery(query))
	print("\n")
	
	file = open("/home/fares/Desktop/data_.txt", "r")
	while True:
		data = file.readline()

		if data == "":
			break
		else:
			data = data[1:-2].split(",")
			to_insert = [data[-1]]
			to_insert += data[:-1] 
			print(to_insert, db.insertRow(to_insert))

	db.close()
#187826