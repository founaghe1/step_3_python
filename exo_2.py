# Verification de l'age 

class Personne:
    def __init__(self, nom, age) -> None:
        self.nom = nom
        self.age = age
        print(f"Bonjour; mon nom est {nom} et j'ai {age} ans")
        
    def afficher_info(self):
        print(f"Nom personne: {self.nom}; et Age personne: {self.age}")
        if  Personne.IsMajeur(self):
            print("je suis majeure")
        else :
            print("Je suis mineure")
        
    def IsMajeur(self):
        if (self.age >= 18):
            return True
        return False
        
        
personne1 = Personne("Mohamed", 25)
personne1.afficher_info()
personne2 = Personne("Ali", 15)
personne2.afficher_info()

print(f"Est majeur : {personne1.IsMajeur()}")
print(f"Est majeur : {personne2.IsMajeur()}")