# La programmation Imperative
''' 
def infos_personnelles(nom, age):
    print(f"Vous vous appelez {nom} et vous avez {age} ans")
    
def demander_nom_personne():
    nom = input("Donnez votre nom : ")
    return nom
    
nom1 = "Moha"
age1 = 25
nom2 = "Alice"
age2 = 30

nom3 = demander_nom_personne()
age3 = 20

infos_personnelles(nom1, age1)
infos_personnelles(nom2, age2)
infos_personnelles(nom3, age3)
'''

# La programmation Orienté Objet

#Creation d'un classe Personne
class Personne:
    #Creation de constructeur
    def __init__(self, nom, age):
        self.nom = nom #Creation d'une variable d'instance: nom
        self.age = age #Creation d'une variable d'instance: age
        print(f"Bonjour mon nom est {nom} et j'ai {age} ans")
        
    # Creation de la methodepresentation
    def Presentation(self):
        print(f"Je suis {self.nom}, j'ai {self.age} ans")

#Utilisation
personne1 = Personne("Moha", 25) #Creation de personne1
personne2 = Personne("Oldia", 33) #Creation de personne2

personne1.Presentation() #Methode d'instance
personne2.Presentation()