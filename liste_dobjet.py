# Creer des collections

class Personne:
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
        
        
personne1 = Personne("Mohamed", 25)
personne2 = Personne("Ali", 15)
#personne3 = Personne()
#personne4 = Personne(age=10)

#personne1.afficher_info()
#personne2.afficher_info()
#personne3.afficher_info()
#personne4.afficher_info()

# Creation des collections
#list_personnes = (personne1, personne2)
list_personnes = [Personne("Mohamed", 25), Personne("Ali", 15), Personne()]

print('Liste 1')
for personne in list_personnes:
    personne.afficher_info()

print('Liste 2')
personne4 = Personne(age=10)
list_personnes.append(personne4)

for personne in list_personnes:
    personne.afficher_info()



#print(f"Est majeur : {personne1.IsMajeur()}")
#print(f"Est majeur : {personne2.IsMajeur()}")