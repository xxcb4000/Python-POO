

from abc import ABC, abstractmethod
import time
import random
import uuid

# Classe abstraite
class Machine(ABC):
    @abstractmethod
    def traiter(self, produit):
        pass

# Représente un bloc de béton avec historique
class Produit:
    def __init__(self, type_bloc):
        self.id = str(uuid.uuid4())[:8]
        self.type_bloc = type_bloc
        self.log = []

    def ajouter_log(self, machine, état):
        horodatage = time.strftime("%H:%M:%S")
        self.log.append(f"[{horodatage}] {machine}: {état}")

# Machines concrètes
class MélangeurBéton(Machine):
    def traiter(self, produit):
        produit.ajouter_log("Mélangeur", "Mélange des matières premières")
        time.sleep(0.2)
        if random.random() < 0.02:
            raise Exception("Panne du mélangeur")
        return produit

class PresseBlocs(Machine):
    def traiter(self, produit):
        produit.ajouter_log("Presse", "Pressage en cours")
        time.sleep(0.3)
        if random.random() < 0.05:
            raise Exception("Bloc mal formé")
        return produit

class Sécheur(Machine):
    def traiter(self, produit):
        produit.ajouter_log("Sécheur", "Séchage à 50°C")
        time.sleep(0.2)
        return produit

class ContrôleQualité(Machine):
    def traiter(self, produit):
        produit.ajouter_log("ContrôleQualité", "Inspection visuelle")
        time.sleep(0.1)
        if random.random() < 0.05:
            raise Exception("Bloc non conforme : fissure détectée")
        produit.ajouter_log("ContrôleQualité", "Bloc validé")
        return produit

# Pipeline
pipeline = [
    MélangeurBéton(),
    PresseBlocs(),
    Sécheur(),
    ContrôleQualité()
]

# Simulation d’une ligne de production
def exécuter_ligne_production(type_bloc):
    produit = Produit(type_bloc)
    try:
        for machine in pipeline:
            produit = machine.traiter(produit)
        print(f"✅ Bloc produit avec succès : ID {produit.id}")
    except Exception as e:
        produit.ajouter_log("ERREUR", str(e))
        print(f"❌ Échec de production : {e} (ID {produit.id})")

    print("📋 Journal de production :")
    for ligne in produit.log:
        print(ligne)

# Exemple d'exécution
if __name__ == "__main__":
    exécuter_ligne_production("Bloc creux")