import requests
from PIL import Image
from pytesseract import image_to_string

'''
https://files.pythonhosted.org/packages/8d/b7/c4fae9af5842f69d9c45bf1195a94aec090628535c102894552a7a7dbe6c/tesseract-0.1.3.tar.gz
'''
        
def uniTel(tel, code):
	"""
	The phone number is nuder normal format
	therefore I'll unify it to the following
	format: 00 yyy XXX XXX XXX.
	"""

	return "00" + code + tel[1:]


def imgToText(image):
	"""
	A function to extract text from image file.
	In my case to extract the phone number.
	
	not mine, found it.
	"""

	img = Image.open(image)
	text = image_to_string(img)

	return text


def downloadImg(link, file_name="phone"):
	"""
	To download the image that contains the phone number
	from the web, so we later on extract the number
	from the image.
	"""

	with open(file_name + ".jpg", 'wb') as f:
		f.write(requests.get(link).content)


if __name__ == '__main__':
	imgToText("/home/fares/Music/phones/cache/divers/38/phone0.jpg")