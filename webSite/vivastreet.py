from bs4 import BeautifulSoup
import requests
import re

GLOABL_PAGE = ""


SEARCH_LINK = "https://search.vivastreet.com/{}/fr/t+{}"

cat = ["autos-motos-bateaux", "bebes-puericulture", "engins-materiels-pro", "chien-chat",
"tous-autres", "vente-maison", "vente-multimedia", "vente-loisirs", "annonces-immobilier"]

def getNum(page_link):
	"""
	To extract the phone number, and the region
	"""
	html = requests.get(str(page_link), stream=True)
	html = BeautifulSoup(html.text, 'html.parser')
	
	phone = html.find("span", {"class":"phone_link"})
	phone = re.findall(r'data-phone-number="([0-9]*)"', str(phone))
	
	region = html.find("div", {"class":"kiwii-no-link-color kiwii-no-link-decoration"})
	region = re.findall(r'<div class="kiwii-no-link-color kiwii-no-link-decoration">(.*)<br/>.*<br/>.*</div>', str(region))
	
	try:		
		region = region[0].split("<br/>")
		return [phone[0], region[0]]
	except Exception as e:
		print("----------")
		return None


def getLinks(link):
	"""
	To extract the links that directs us to the
	the pages, so we can download the images that
	contains the phone numbers.
	:param link:
	:return:
	"""
	global GLOABL_PAGE
	
	html = requests.get(link)
	html = BeautifulSoup(html.text, 'html.parser')

	GLOABL_PAGE = html.text
	
	a_link = html.find_all("a", {"class":"clad__wrapper"}, href=True)

	for l in a_link:
		yield l["href"]



def fetch(cat, skip=-1):
	file = open(cat + ".txt", "a")

	counter = 0

	# init the process
	page_counter = 1
	out = False

	while out is False:
		# make the search link
		search_link = SEARCH_LINK.format(cat, page_counter)

		while True:
			try: 
				for link in getLinks(search_link):
					if counter <= skip:
						print(counter, "Page::", page_counter)
						counter += 1
						continue

					num = getNum(link)

					if num is not None:
						file.write(str(num))
						file.write("\n")
						print(counter, "Page::", page_counter, "Category::", cat)
						# print(str(num))
						counter += 1
				break
			except:
				pass
			
		if "Suivante" not in GLOABL_PAGE:
			out = True
		else:
			page_counter += 1

	file.close()


if __name__ == '__main__':
	#fetch("vente-loisirs")
	pass
