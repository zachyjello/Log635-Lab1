# Rule.py

from aima.logic import FolKB, expr, fol_bc_ask 

# Liste des personnages, armes, et lieux impliqués
personnages = ["Pikachu", "Evoli", "Dracaufeu", "Ectoplasma", "Carapuce", "Herbizarre"]
lieux = ["Bourg Palette", "Azuria", "Jadielle", "Lavanville", "Celadopole", "Rotombourg"]
armes = ["BatteBaseballAvecClous", "WaterGun", "LanceFlamme", "Tronçonneuse", "Poison", "Grenade"]

class ReglesInference:
    def __init__(self):
        self.clauses = []
        self.define_rules()
        

    def define_rules(self):
        # la pièce du crime
        self.clauses.append(expr('EstMort(x) & Personne_Piece(x, y) ==> PieceCrime(y)'))

        # l'arme du crime
        self.clauses.append(expr('PieceCrime(x) & Arme(y) & Arme_Piece(y, x) ==> ArmeCrime(y)'))
        self.clauses.append(expr("EstMort(x) & MarqueCou(x) ==> ArmeCrime(Corde)"))

        # Si une personne est morte, elle est la victime et innocente
        self.clauses.append(expr('EstMort(x) ==> Victime(x)'))
        self.clauses.append(expr('EstMort(x) ==> Innocent(x)'))

        # Si une personne vivante était dans une pièce sans l'arme du crime, elle est innocente
        self.clauses.append(expr(
            'EstVivant(p) & UneHeureApresCrime(h1) & Personne_Piece_Heure(p, r2, h1) & PieceCrime(r1)'
            ' & PieceDifferente(r1, r2) & ArmeCrime(a1) & Arme_Piece(a2, r2) & ArmeDifferente(a1, a2) ==> Innocent(p)'))

        # Si une personne vivante se trouvait dans une pièce avec l'arme du crime, elle est suspecte
        self.clauses.append(expr(
            'EstVivant(p) & UneHeureApresCrime(h1) & Personne_Piece_Heure(p, r2, h1) & PieceCrime(r1)'
            ' & ArmeCrime(a) & Arme_Piece(a, r2) ==> Suspect(p)'))

    def get_clauses(self):
        return self.clauses
    
    def add_fact(self, clause_string):
        self.clauses.append(expr(clause_string))