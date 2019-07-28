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
	"divers"
]
