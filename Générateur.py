
nombre_de_personnage = int(input("combien voulez-vous créer de personnage aléatoire ? : "))

niveau_du_personnage = int(input("de quel niveau voulez-vous vos personnage ? : "))

#nom = [ "Thalador", "Dracaris", "Elowen", "Zephyrion", "Galadria", "Lythandra", "Thundrak", "Arvandus", "Sylveria" ]

nom = ["Thalador", "Dracaris", "Elowen", "Zephyrion", "Galadria", "Lythandra", "Thundrak", "Arvandus", "Sylveria", "Solanar","Valerion", "Elyndra", "Falorian", "Nithralis", "Seraphina", "Caladrius", "Marwen", "Azurian", "Tyllaria", "Fenrisar","Elaris", "Althorin", "Thessalya", "Malachor", "Astridelle", "Orionis", "Selenea", "Bryston", "Eowyn", "Vaeloria","Sorenthor", "Valyndra", "Aeliana", "Galandriel", "Thundorin", "Eilinora", "Arion", "Alveron", "Isolde", "Drakonar","Thalira", "Elarion", "Ravendark", "Silveria", "Seraphiel", "Calandria", "Valandor", "Eldrith", "Arvandor", "Elysara","Thalindra", "Nyxarian", "Thalorin", "Aeloria", "Galadran", "Elariana", "Marvandor", "Thalara", "Elowynne", "Zephyros","Velorian", "Valandria", "Lirael", "Sylvaris", "Seraphina", "Selendria", "Thalador", "Elorin", "Aelarion", "Caladriel","Elaris", "Nethrion", "Tyllarian", "Thandorin", "Arvandria", "Galandor", "Elysium", "Vaelorian", "Valerian","Astridelle", "Lythorin", "Isolde", "Drakaris", "Sylveran", "Thalina", "Valeria", "Eloweth", "Selenea", "Malachar","Thundoril", "Alverian", "Eilinor", "Althorin", "Seraphiel", "Elysara", "Thessalya", "Elarion", "Vaeloria", "Sorenthor","Galadria"]

occupation = ["vidangeur de latrines", "autre chose","serrurier","bedeau","joalier"]

classe = ["clerc", "guerrier", "mage", "archer"]
niveau = niveau_du_personnage
titre = "XXX"
alignement = ["neutre","loyale","chaotique"]
#vitesse (nombre de pas) = []
px = "0"
classe_armure = []
points_de_vie = []
force = []
#modif 
#agiliter + modif = []
#endurance + modif = []
#présence + modif = []
#chance + modif = []
#inteligence + modif = []
#JDS réf = []
#JDS vig = []
#JDS vol = []
#chanceux avec = []
langages = ["le commun","nain","elfe"]
#portrait ou symbole = []
initiative = []
dé_action = []
attaque = []
#dé critique = []
#table critique = []
armes = ["une truelle (dague)","une dague","un baton"]
trésors = []
armure = []
équipement = []
notes = []

import random
# Demande à l'utilisateur de saisir un nombre

for i in range(nombre_de_personnage):
    # Mettez ici le code que vous souhaitez exécuter à chaque itération
    nom_choisi = random.choice(nom)
    occupation_choisi = random.choice(occupation)
    classe_choisi = random.choice(classe)
    alignement_choisi = random.choice(alignement)
    armes_choisi = random.choice(armes)
    print("---------------------------")
    print("personnage numéro", i + 1)
    print("le prénom du perssonage est ",nom_choisi)
    print("l'occupation du perssonage est ",occupation_choisi)
    print("l'alignement du perssonage est ",alignement_choisi)
    print("la classe du perssonage est ",classe_choisi)
    print("le titre du perssonage est ",titre)
    print("le niveau du perssonage est ",niveau)
    print("le px du perssonage est ",px)
    print("l'arme du perssonage est ",armes_choisi) 

# Fin du programme
print("---------------------------")
print("tout les personage on été créer.")
print("---------------------------")
