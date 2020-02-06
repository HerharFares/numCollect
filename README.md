DISCRIPTION:
-
I had the idea to use phone numbers, and may be sell them online,
but hey no use.<br>
Any way, I scaped over 180K Algerien phone number, and over 16k French phone numbers.<br>
The numbers were scraped from online selling websites(like ebay),
***https://ouedkniss.com*** for Algeria, and ***https://vivastreet.com*** for France. In the algerian website, the phone bumbers are stored as images, therefore i had to download the images,so i can extract them later using imageto text. The French website was very simple to deal with.<br>
The phone numbers are stored into CSV, DB end TXT files, you'll find them in the data folder, dataDz for Algeria, dataFr for France, boutiqueDZ.json only a later on idea that contains a list extracted from ***https://ouedkniss.com***.<br>
In the WebSite directory you'll find the scraping code. And some notes and extra code in the use directory.


TOOLS:
-
* Language
	* Python 3.6

* Libraries
	> scraping the websites
	* BeautifulSoup
	> for storing the data
	* Json
	* Sqlite3
	> for image recognetion, image to text
	* Pytesseract
	* Pillow(PIL)


PS:
-
***The data is in the data directory, CSV, Json, Db, and TXT file***