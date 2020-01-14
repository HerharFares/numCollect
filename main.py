import re
from bs4 import BeautifulSoup

from use.tools import *


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


def fetch(cat, wl, skip=-1):
    file = open("try.txt", "a+")

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
                        downloadImg(img_link, "try/" + "/" + wl + "__" + str(counter))
                        file.write(wl + "__" + str(counter) + "     " + an_link)
                        file.write("\n")

                        print(counter, "Page::", page_counter, "Wilaya::", wl, "Category::", cat)
                        counter += 1
                    else:
                        continue
            except Exception as e:
                # raise e
                pass
        else:
            out = True
            continue

        # access the next page
        page_counter += 1


if __name__ == '__main__':
    fetch("immobilier", "Ain+Temouchent", 789)
    for wl in wilayaSearch[46:]:
        fetch("immobilier", wl)
