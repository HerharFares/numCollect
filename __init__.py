from items import *
from tools import *
import time
import os
import res.ouedkniss.ouedkniss as oks


def fetch(cat, wl, skip=-1):
	counter = 0

	# init the process
	page_counter = 1
	out = False
	
	while out is False:
		# make the search link
		link = SEARCH_LINK_PAGE.format(cat, wl, page_counter)
	
		# the links
		links = list(oks.getLinks(link))
		# in this case the page is not valid
		# so we go to next wilaya
		if len(links) != 0:
			for an_link in links:
				if counter <= skip:
					print(counter, "Page::", page_counter)
					counter += 1
					continue
				# get the image link
				img_link = oks.getImgLink(an_link)
					
				# if the link exists, download the image
				if len(img_link) != 0:

					# download the image
					downloadImg(img_link, "cache/" + cat + "/" +
					            str(wilayaSearch.index(wl) + 1)+"/phone" + str(counter))

					print(counter, "Page::", page_counter, "Wilaya::", wl)
					counter += 1
				else:
					continue
		else:
			out = True
			continue
				
		# access the next page
		page_counter += 1


def scritch():
	file = open("/home/fares/Desktop/data.txt", 'a')
	
	for cat in category:
	 	for wl in range(1, 49):
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

if __name__ == "__main__":

	scritch()


	