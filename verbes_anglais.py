
# vise à tester les verbes irréguliers - ebauche
# dictionnaire des verbes irréguliers à compléter
my_dict = { 
	"frapper" : ["hit","hit","hit"],
	"voler" : ["steal", "slole","stolen"]
	}


# fonction pour tester les verbes irréguliers
# on rentre la base_verbale sans le to, le preterit et participe_passe
def test(verbe,tableau): 
	print("merci de conjuguer en anglais le verbe ",verbe)
	base_verbale = input("saisir base_verbale : ")
	preterit = input("puis  preterit : ")
	participe_passé = input("puis participe_passé : ")
	list_reponse = [base_verbale, preterit, participe_passé]
#	print(*list_reponse,sep ='\n')
	if tableau == list_reponse :
		print("bravo")
	else :
		print("la bonne réponse est:",*tableau)
#

# fonction test 2 vise à saisir les réponses séparé d'un espace.
# pas encore implémenté 
def test2(verbe,tableau): 
	print("merci de conjuguer en anglais le verbe ",verbe)
	reponse = input("saisir base_verbale : ")
	list_reponse = reponse.split(reponse)
#	print(*list_reponse,sep ='\n')
	if tableau == list_reponse :
		print("bravo")
	else :
		print("la bonne réponse est:",*tableau)
#


#test de la fonction 
test("frapper",my_dict["frapper"])

