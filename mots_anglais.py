import random

# je rentre les mots du dictionnaire pour l'instant 
# dans une version ultèrieure, on pourra le mettre dans un fichier - peut-etre json
dico_fr_en = {
	"il y a " : "there is",
	"il y a - pluriels :" : "there are",
	"pays" : "country",
	"le Royaume Uni" : "the United Kingdom",
	"le Royaume Uni(abr)" : "UK", 
	"Angleterre" : "England",
	"Pays de Galles" : "Wales",
	"Ecosse" : "Scotland",
	"Irlande du Nord" : "Northern Ireland",
	"parler" : "to speak",
	"famille" : "family",
	"lumière" : "light",
	"penser" : "to think",
	"américain" : "American",
	"Les États Unis d'Amérique" : "The United States of America ( USA )",
	"britannique" : "british",
	"premier" : "first",
	"excité/impatient" : "excited",
	"nerveux" : "nervous",
	"Irlande" : "Ireland",
	"Irlandais" : "Irish",
	"Ecossais" : "Scottish",
	"se souvenir" : "to remember",
	"le 2ème" : "the second",
	"le troisème" : "the third",
	"où" : "Where",
	"écrire" : "to write",
	"principal directeur" : "head teacher",
	"professeur" : "teacher",
	"arbre" : "tree",
	"élève" : "pupil",
	"élève" : "student",
	"onze" : "eleven",
	"douze" : "twelve",
	"treize" : "thirteen",
	"prénom" : "first name",
	"nom de famille" : "last name",
	"quand" : "When",
	"quel âge" : "how old",
	"chanson" : "song",
	"chanter" : "to sing",
	"super" : "great",
	"les 2" : "both",
	"deviner" : "to guess",
	"lire" : "to read",
	"souligner" : "to underline",
	"enfants" : "children", 
	"site internet" : "website",
	"photo" : "picture",
	"mille" : "thousand",
	"cent" : "hundred", 
	"plan"  : "map", 
	"carte" : "map", 
	"phrase" : "sentence",
	"vrai" : "true",
	"faux" : "false",
	"bibliothèque" : "library",
	"piscine" : "swimming pool",
	"gymnase" : "gym",
	"vestiaire" : "changing room",
	"cour de recré" : "playground",
	"peau" : "skin",
	"hauteur" : "height",
	"construire" : "to build",
	"carrure" : "build",
	"chère" : "dear",
	"matière scolaire" : "school subject",
	"EPS" : "physical education",
	"ami" : "friend",
	"meilleur ami" : "best friend",
	"habiter" : "to live",
	"beau-frère" : "halfbrother",
	"belle-mère" : "stepmother",
	"demi-soeur" : "halfsister",
	"demi-frère" : "",
	"petit ami" : "boyfriend",
	"petite amie" : "girlfriend",
	"nièce" : "niece",
	"neveu" : "nephew",
	"église" : "church",
	"marcher" : "to walk",
	"bagues dentaires" : "braces",
	"après" : "after",
	"aller" : "to go",
	"donc"  : "so",
	"SMS" : "text message",
	"s'inquiéter" : "to worry", 
	"demain" : "tomorrow",
	"étuduer" : "to study",
	"vouloir" : "to want",
	"plus" : "more",
	"parce que" : "because",
	"to get up" : "se lever",
	"to have breakfast" : "prendre le petit déjeuner",
	"to brush" : "brosser", 
	"une dent" : "a tooth",
	"des dents" : "teeth",
	"s'habiller" : "to get dressed",
	"courrir" : "to run",
	"prendre une douche" : "to have a shower",
	"se réveiller" : "to wake up",
	"laver" : "to wash",
	"visage" : "face",
	"before" : "avant", 
	"tous les jours" : "everyday",
	"half" : "demi",
	"to hate" : 'détester',
	"thirty" : "trente",
	"break" : "pause",
	"to have lunch" : "déjeuner",
	"to have dinner" : "diner",
	"evening" : "soir",
	"always" : "toujours"

	}

# Je crée des listes a partir du dictionnaire
list_french = list (dico_fr_en.keys())
list_english = list(dico_fr_en.values())

# Je tire au sort un nombtre
nombre_mots_dic = len(list_french)
print("Il y a", nombre_mots_dic," mots dans le dictionnaire")

#initialise les variables 
i = 1 
list_tirage = [] #liste des mots tirés 

# je tire 10 mots 
while ( i <= 10 ):
	i = i + 1
	tirage = random.randrange(0, nombre_mots_dic)
	if tirage in list_tirage : 
		tirage = random.randrange(0, nombre_mots_dic)
		list_tirage.append(tirage)
	else : 
		list_tirage.append(tirage)

#	print(tirage)
	print("Trouver moi le mot anglais correspondant à :", list_french[tirage])
	user_answer = input()
	if user_answer == list_english[tirage]:
		print('bravo') 
	else: 
 		print('faux, la bonne réponse est :', list_english[tirage])



#je réinterroge une deuxième fois sur les mots faux 