from webSite.ouedkniss import *


SEARCH_LINK = "https://www.ouedkniss.com/boutiques/stores.php?store=&c={}&wilaya={}"
CONTACT_LINK = "https://www.ouedkniss.com/store/contact.php?id={}"


def find_store_id(page_link):
	"""
	To extract the idS of the stores.
	:param page_link:
	:return:
	"""
	html = requests.get(page_link, stream=True)
	html = BeautifulSoup(html.text, 'html.parser')
	
	links = html.find_all("a", class_="store_name")

	for link in links:
		yield re.findall(r'id=(\d*)', link["href"])[0]


def find_store_info(page_link):
	"""
	To extract the idS of the stores.
	:param page_link:
	:return:
	"""
	html = requests.get(page_link, stream=True)
	html = BeautifulSoup(html.text, 'html.parser')

	links = html.find("div", {"id": "footer_store"})
	links = str(links.text).replace("\t", "")


	print(links)


if __name__ == '__main__':
	pass
	find_store_info("https://www.ouedkniss.com/store/contact.php?id=6275")
