# La notion d'heritage

#Classe parent
class EtreVivant:
    espece_etre_vivant = "espece non identifié"
    
    def AfficheEspece(self):
        print("Espece :", self.espece_etre_vivant)

#classe enfant de classe EtreVivant
class Chat(EtreVivant):
    espece_etre_vivant = "Chat (Mamifere felin)"
    
#classe enfant de classe EtreVivant
class Personne(EtreVivant):
    #Creation de la variable de classe
    espece_etre_vivant = "Humain (Mamifere homo sapiens)"
    
    
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
       

#classe enfant de la classe Personne
class Etudiant(Personne):
    def __init__(self, nom, age, etudes):
        #self.nom = nom
        #self.age = age
        super().__init__(nom, age)
        self.etude = etudes
        
    def afficher_info(self):
        super().afficher_info()
        print("Je suis", self.etude)
        

list_personnes = [Personne("Mohamed", 25), Personne("Ali", 15), Personne("Zoe", 18)]

print('Liste 1')
for personne in list_personnes:
    personne.afficher_info()
    personne.AfficheEspece()
    print()
    
chat = Chat()
chat.AfficheEspece()

etudiant = Etudiant("Mario", 24, "étudiant à Bakeli")
etudiant.afficher_info()
etudiant.AfficheEspece()

