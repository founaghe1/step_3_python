# les variables de classe

class Personne:
    #Creation de la variable de classe
    espece_etre_vivant = "Humain (Mamifere)"
    
    
    def __init__(self, nom = "", age = 0):
        self.nom = nom
        self.age = age
        if nom == "":
            self.DemanderNom()
        print(f"Nom personne: {self.nom}")
        
    def afficher_info(self):
        nom_personne = "Bonjour; mon nom est: " + self.nom
        if self.age != 0:
            nom_personne += ", j'ai " + str(self.age) + " ans"
        print(nom_personne)
        if self.age != 0:
            if  Personne.IsMajeur(self):
                print("je suis majeure")
            else :
                print("Je suis mineure")
        
    def IsMajeur(self):
        if (self.age >= 18):
            return True
        return False
    
    def DemanderNom(self):
       self.nom = input('Entrez votre nom : ')
       
    def AfficheEspece():
        print("Espece :", Personne.espece_etre_vivant)
        
        

list_personnes = [Personne("Mohamed", 25), Personne("Ali", 15), Personne("Zoe", 18)]

print('Liste 1')
for personne in list_personnes:
    personne.afficher_info()
    Personne.AfficheEspece()
    print()

