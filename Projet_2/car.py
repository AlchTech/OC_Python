class Voiture:

  def __init__(self, moteur, couleur, modele):
    self.moteur = moteur
    self.couleur = couleur
    self.modele = modele

  def demarre(self, bruit = "vroom"):
    return bruit

  def model(self):
    return self.modele




voiture1 = Voiture(12, "rouge", "Tesla")            # Declare un objet
voiture2 = Voiture(6, "noire", "Renauld")            # Declare un objet

print(voiture1)
print(voiture1.moteur)                      
print(voiture1.couleur)

print(voiture1.demarre())
print(voiture1.model())