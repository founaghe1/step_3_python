class Personne:
    def __init__(self, nom, age) -> None:
        self.nom = nom
        self.age = age
        print(f"Bonjour; mon nom est {nom} et j'ai {age} ans")
        
    def afficher_info(self):
        print(f"Nom personne: {self.nom}; et Age personne: {self.age}")
        
        
personne1 = Personne("Mohamed", 25)
personne1.afficher_info()
personne2 = Personne("Ali", 33)
personne2.afficher_info()