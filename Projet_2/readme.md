# Python

## 1. Apprenez les bases du langage Python

STOCKAGE DES DONNEES :

```CODE
VARIABLE :
nom_variable = valeur

print(nom_variable)                 # VOIR VALEUR ASSOCIER VARIABLE
print(type(nom_variable))           # VOIR LE TYPE DE VALEUR ASSOCIER VARIABLE

<!-- Le nom doit être descriptif et ne pas trop abreger ce derniere -->
<!-- Utiliser la convention 'snake_case' pour la nommée  -->
<!-- N'utiliser pas d'accent -->
<!-- Il est sensible a la case : Age, AGE, age sont des variables différentes    -->

TYPE DE VALEUR :
    CHAINE :
    nom_variable = "texte"                   # CHAINE | STRING
    nom_variable = str(5)                    # CHAINE | STRING

        OPERATION CHAINE :
        name_variable = "va" + "riable"      # CONCATENATION
        name_variable.lower()                # MINISCULE
        name_variable.upper()                # MAJUSCULE
        name_variable.capitalize()           # CAPITALISATION
        name_variable.replace(old, new)      # REMPLACE OLD PAR NEW
        name_variable.find(mot)              # RECHERCHE ET RETOURNE LA PHRASE CONTENANT MOT

    NUMERIC :
        nom_variable = 1                     # NUMERIC | ENTIER
        nom_variable = int("1")              # NUMERIC | ENTIER
        nom_variable = 1.0                   # NUMERIC | FLOAT
        nom_variable = float("1")            # NUMERIC | ENTIER

        OPERATION NUMERIC :
            nom_variable = 5 + 2             # ADDITION
            nom_variable = 5 - 2             # SOUSTRACTION
            nom_variable = 5 * 2             # MULTIPLICATION
            nom_variable = 5 / 2             # DIVISION RESULTAT FLOAT
            nom_variable = 5 / 2             # DIVISION RESULTAT INTEGER²
            nom_variable = 5 % 2             # DIVISION RESTE
            nom_variable = 5 ** 5            # PUISSANCE
            nom_variable = abs(-5)           # VALEUR ABSOLUE 
            nom_variable = random()          # ALEATOIRE

    BOOL :
        nom_variable = True                  # BOOLEAN | VRAI
        nom_variable = False                 # BOOLEAN | FAUX

    LIST :
        nom_variable = [1, 2, 3, 4, 5]       # TABLEAU DE VALEUR MODIFIABLE
        nom_variable = ["a", "b", "c"]       # TABLEAU DE VALEUR MODIFIABLE
        nom_variable = [True, False, False]  # TABLEAU DE VALEUR MODIFIABLE

            OPERATION LIST :
                nom_variable.append(6)       # AJOUTE UN ENTIER A LA LISTE
                nom_variable.insert(1, text) # AJOUTE TEXTE A L'INDEX 1
                nom_variable.extend([1, 2])  # AJOUTE UNE LISTE A UNE AUTRE LISTE
                nom_variable.index(text)     # RETOURNE L'INDEX OU SE TROUVE TEXT
                nom_variable.remove("b")     # SUPPRIME STRING "b" DANS LA LISTE
                del nom_variable[3]          # SUPPRIME ELEMENT A L'INDEX 3
                len(nom_variable)            # NOMBRE D'ELEMENT DANS LA LISTE
                nom_variable.sort()          # TRI PAR ORDRE ALPHABETIQUE


    TURPLE :
        nom_variable = (1, 2, 3, 4, 5)       # TABLEAU DE VALEUR NON MODIFIABLE
        nom_variable = ("a", "b", "c")       # TABLEAU DE VALEUR NON MODIFIABLE
        nom_variable = (True, False, False)  # TABLEAU DE VALEUR NON MODIFIABLE

    DICTIONNAIRE :
        nom_variable = {                     # DICTIONNAIRE AVEC SES KEY : VALUE
            "voiture": "Tesla",              # DICTIONNAIRE AVEC SES KEY : VALUE
            "vélo": "Nakamura"               # DICTIONNAIRE AVEC SES KEY : VALUE
            "other: [1, 2, 3]                # DICTIONNAIRE AVEC SES KEY : VALUE
            }                                # DICTIONNAIRE AVEC SES KEY : VALUE
        nom_variable = dict{
            key: value,
            key: value
        }
        print(nom_variable["voiture"])       # Tesla
        print(nom_variable[key[0]])          # voiture
        print(nom_variable[value[0]])        # Tesla
        print(nom_variable[key])             # voiture, vélo
        print(nom_variable[value])           # Tesla, Nakamura

            OPERATION DICTIONNAIRE :
                nom_variable["texte"] = Z    # AJOUTE UN VALEUR KEY AU DICTIONNAIRE
                nom_variable.pop["key"]      # RENVOIE LA VALEUR DE LA KEY SUPPRIME
                del.nom_variable["key"]      # SUPPRIME LA KEY ET SA VALEUR
                "key" in nom_variable        # VERIFIE SI KEY EXIST ET RENVOIE VALEUR

```

CONDITION :

```code

IF | ELIF | ELSE :
if(variable1 == variable2):                   # SI TRUE EXECUTE CODE
    print("A")
elif(variable1 <= variable2):                 # SI "IF" EST FALSE VERIFIE CONDITION
    print("B")
elif(variable1 <= variable2):                 # SI "ELIF" EST FALSE VERIFIE CONDITION
    print("C")
else:                                         # SI AUCUNE CONDITION FONCTIONNE
    print("D")

    OPERATEUR LOGIQUE :
        if variable1 and variable2:           # SI LES DEUX VARIABLES SONT TRUE ALORS A
            print("A")
        if variable1 or variable2:            # SI UNE VARIABLES EST TRUE ALORS B
            print("B")
        if variable1 and not variable2:       # SI AUCUNE ET TRUE ALORS
            print("C")

    EXPRESSION COMPARATIVE :
        if variable1 == variable2             # SI VAR1 EST EGALE A VAR2 ALORS
        if variable1 != variable2             # SI VAR1 N'EST PAS EGALE A VAR2 ALORS
        if variable1 < variable2              # SI VAR1 INFERIEUR A VAR2 ALORS
        if variable1 <= variable2             # SI VAR1 INFERIEUR OU EGAL A VAR2 ALORS
        if variable1 >= variable2             # SI VAR1 SUPERIEUR OU EGAL A VAR2 ALORS
        if variable1 > variable2              # SI VAR1 SUPERIEUR A VAR2 ALORS
```

BOUCLE :

```code
BOUCLE FOR:
    #1
    for name_value in name_list:              # PARCOURE UNE LISTE
        print(name_value)                     # IMPRIMERA CHACUNE DES VALEURS DANS LIST

    #2
    for x in range(100):                      # REPETE LA BOUCLE 100 FOIS
        print(f"{x} bouteilles pleine !")     # f"{x}" RENVOIE LE RESULTAT EN COURS

    #3
    for x in range(5 10):                      # REPETE LA BOUCLE 5 FOIS A PARTIR DE 5
        print(f"{x} bouteilles pleine !")      # f"{x}" RENVOIE LE RESULTAT EN COURS

BOUCLE WHILE:
    #1
    while True:                                # REPETE TANT QUE VRAI

    #2
    x = 0                                      # INITALISE UNE VARIABLE
    while x != 5:                              # REPETE X TANT QUE DIFFERENT DE 5
        x += 1                                 # INCREMENTE X DE 1
```

FUNCTION

```code
DELACARATION_FUNCTION :
    #1 ARGUMENT SIMPLE
        def name_Function(arg1):               # FUNCTION A UN ARGUMENT
            variable1 = arg1                   # ASSIGNE VALEUR A ARG1 A LA VARIABLE
            print(arg1)                        # AFFICHERA VALEUR DE ARG1

    #2 ARGUMENT MULTIPLE
        def name_Function(arg1, arg2):         # FUNCTION A DEUX ARGUMENT OU PLUS
            variable1 = arg1
            variable2 = arg2
            variable3 = variable1 + variable2
            return variable3                   # RETOURNERA LA VALEUR ISSU DE ADDITION OU CONCATENATION


APPEL_FUNCTION :
    #1 ARGUMENT SIMPLE
        name_Function("Hello")                 # Hello

    #2 ARGUMENT MULTIPLE
        name_Function(5, 3)                    # 8

    #3 VOIR DOC FUNCTION
    help(name_Function)

```

LES CLASSES

Une classe est en quelque sorte le schéma de construction d’un objet qui va définir les caractéristiques de tous les objets de ce type et leurs fonctionnalités.

```CODE
class Voiture:

  def __init__(self, moteur, couleur, modele):      # Attribut
    self.moteur = moteur
    self.couleur = couleur
    self.modele = modele

  def demarre(self, bruit = "vroom"):               Methode demarre
    return bruit

  def model(self):                                  Methode model
    return self.modele




voiture1 = Voiture(12, "rouge", "Tesla")             # Declare un objet
voiture2 = Voiture(6, "noire", "Renauld")            # Declare un objet

print(voiture1)                                      # <__main__.Voiture object at 0x000001A41725FCA0>
print(voiture1.moteur)                               # 12                      
print(voiture1.couleur)                              # rouge

print(voiture1.demarre())                            # vroom
print(voiture1.model())                              # Tesla
```

LES_PACKAGES ET IMPORTATION

```CODE
PACKAGES :
    pip install <nom-du-package>                    # PERMET D'INSTALLER UN PACKAGE
    pip freeze                                      # PERMET DE VOIR LES PAQUETS DEJA INSTALLER

IMPORTATION :
    import <nom-du-package>                         # PERMET D'IMPORT DES FUNCTIONS DANS VOTRE FICHIER
    from <nom-du-package>  import <nom-function>    # PERMET D'IMPORT UNE FUNCTIONS DANS VOTRE FICHIER

STRUCTURE_PACKAGE :
    |-geometrie
            |- __init__.py
            |- fonction.py
            |- classes.py
            |- variable.py


LIST_PACKAGE :
    SCRAPING :
        Beautiful Soup                              # PERMET RECUPERER DES DONNEES DES FICHIER HTML ET XML

    API :
        Requests                                    # PERMET RECUPER DE FAIRE APPELS INTERFACE REST

    DATASCIENCE :
        Pandas                                          # PERMET ANALYSE ET MANIPULATION DONNEES
```

---

EXTRACTION DE DONNEES :

```CODE
from pyclbr import Function
import requests                         # Requests permettant de récupérer les données de l'API ou site web
from bs4 import BeautifulSoup           # BeautifulSoup permettant de parser(traiter) le code HTML

page = requests.get("https://www.gov.uk/search/news-and-communications")    # Récupération de la page
soup = BeautifulSoup(page.content, 'html.parser')                           # Parsing du code HTML

# ELEMENT HTML
print(soup.div)                          # Affiche premier element div de la page
print(soup.h1)                           # Affiche premier element h1 de la page
print(soup.title)                        # Affiche le titre de la page
print(soup.find_all("div"))              # Affiche tous les elements div de la page
print(soup.find_all("h1"))               # Affiche tous les elements h1 de la page
print(soup.find_all("p"))                # Affiche tous les elements p de la page
print(soup.find_all(['h1', 'a', 'p']))   # Affiche tous les elements h1, a et p de la page
...

# TEXTE
print(soup.div.string)                  # Affiche le contenu du premier element div de la page
print(soup.h1.string)                   # Affiche le contenu du premier element h1 de la page
print(soup.title.string)                # Affiche le contenu du titre de la page


# ATTRIBUT
print(soup.div.attrs)                    # Affiche les attributs de l'element div
print(soup.h1.attrs)                     # Affiche les attributs de l'element h1
print(soup.title.attrs)                  # Affiche les attributs de l'element title
...

# CLASS
print(soup.div.attrs['class'])          # Affiche la valeur de l'attribut class de l'element div
print(soup.h1.attrs['class'])           # Affiche la valeur de l'attribut class de l'element h1
print(soup.title.attrs['class'])        # Affiche la valeur de l'attribut class de l'element title
print(soup.find_all(attrs={'class':'b', 'id':'a'})) # Affiche tous les elements ayant les attributs class=b et id=a
print(soup.select('title'))             # Affiche la valeur de l'attribut class de l'element title
...

# ID
print(soup.div.attrs['id'])             # Affiche la valeur de l'attribut id de l'element div
print(soup.h1.attrs['id'])              # Affiche la valeur de l'attribut id de l'element h1
print(soup.title.attrs['id'])           # Affiche la valeur de l'attribut id de l'element title
print(soup.find_all(attrs={'class':'b', 'id':'a'})) # Affiche tous les elements ayant les attributs class=b et id=a
print(soup.select("#selected"))         # Affiche la valeur de l'attribut id de l'element selected

# NAME
print(soup.div.name)                    # Affiche le nom de l'element div
print(soup.h1.attrs['name'])            # Affiche le nom de l'element h1
print(soup.title.attrs['name'])         # Affiche le nom de l'element title


# BOUCLE
for child in soup.ul.children:              # Parcours tous les enfants de l'element ul
    print(child)                            # Affiche tous les enfants(li) de l'element ul

for link in soup.select(".recipeLink > a"): # Affiche tous les elements a de la classe recipeLink
  webpage = requests.get(link)              # Récupération de la page
  new_soup = BeautifulSoup(webpage)         # Parsing du code HTML

for link in soup.find_all('a'):             # Affiche tous les elements "a" de la page
    print(link.get('href'))                 # Affiche l'attribut href de tous les elements "a"


titres_bs = soup.find_all("a", class_="lien")   
titres = []
for titre in titres_bs:
    titres.append(titre.string)

# REGEX
import re
soup.find_all(re.compile("[ou]l"))      # Affiche tous les elements ul ou ol de la page
soup.find_all(re.compile("h[1-9]"))     # Affiche tous les elements h1 à h9 de la page

# FONCTION
def retourne_class(tag):                # Fonction qui retourne la valeur de l'attribut class d'un element
    return tag.attr('class') == "A"     # Retourne True si l'attribut class de l'element est égal à A

soup.find_all(retourne_class)           # Affiche tous les elements ayant l'attribut class égal à A

```

CHARGEE DONNEES (lire données types .txt et .csv.):

```CODE
TEXTE :
    fichier = open("./fichier.txt", "mode")
        mode :
            "r"                # Lire
            "w"                # Écrire (écraser) :
            "a"                # Continuer d’écrire
            "r+"               # Lire et écrire (écraser)

    EXEMPLE FERMETURE MANUELLE(close):
        fichier = open("hello.txt", "w")
        fichier.write("Hello, world!")
        fichier.close()

    EXEMPLE FERMETURE AUTO(with) :
        with open("file.txt") as fichier:
        for ligne in fichier:
            # faire quelque chose avec une ligne
            print(ligne)

CSV :
    import csv

    LECTURE LIST :
        with open('couleurs_preferees.csv') as fichier_csv:
        reader = csv.reader(fichier_csv, delimiter=',')
        for ligne in reader:
            print(ligne)

    LECTURE DICTIONNAIRE :
        with open('couleurs_preferees.csv') as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=',')
        for ligne in reader:
            print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + ")

    SAUVEGARDE CSV :
        en_tete = ["titre", "description"]              # Créer une liste pour les en-têtes

        with open('data.csv', 'w') as fichier_csv:      # appel csv en mode ecriture
        writer = csv.writer(fichier_csv, delimiter=',') # Créer un objet writer (écriture) avec ce fichier

        writer.writerow(en_tete)                        # Créer l'en-têtes

        # Parcourir les titres et descriptions (zip permet d'itérer sur deux listes ou plus à la fois)
        for titre, description in zip(titres, descriptions):
            ligne = [titre, description]
            
            writer.writerow(ligne)                      # Créer une nouvelle ligne data dans tites et description

    EXCEL :
        OUVRIR EXCEL
            - DATA
            - GET EXETERNAL
                - FROM TEXTE
                - SELECTIONNE FICHIER.CSV
                - DELIMTED "COMMA"
                - FINISH

    EXEMPLE COMPLET
        import requests
        from bs4 import BeautifulSoup
        import csv

        # lien de la page à scrapper
        url = "https://www.gov.uk/search/news-and-communications"
        reponse = requests.get(url)
        page = reponse.content

        # affiche la page HTML
        print(page)

        # transforme (parse) le HTML en objet BeautifulSoup
        soup = BeautifulSoup(page, "html.parser")

        # récupération de tous les titres
        titres = soup.find_all("a", class_="gem-c-document-list__item-link")
        titre_textes = []
        for titre in titres:
            titre_textes.append(titre.string)

        # récupération de toutes les descriptions
        descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
        description_textes = []
        for description in descriptions:
            description_textes.append(description.string)

LEGALITE ET ETHIQUE :

Les sites web n’ont pas tous des politiques qui autorisent d’extraire leurs données. Pour savoir si une entreprise l’autorise, assurez-vous de vérifier leurs Conditions générales. "facebook.com/robots.txt"

Utilisez une interface publique si possible et si disponible. Plus de détails sur les interfaces sont disponibles dans le cours Adoptez les API REST pour vos projets web.

Fournissez un agent utilisateur dans l’en-tête de votre requête pour vous identifier en tant que développeur qui extraie de façon éthique.

Créditez toujours le propriétaire pour éviter les problèmes de copyright.

Ne faites pas des requêtes de données trop souvent.
```

JUPITER :

```CODE
LANCER JUPYTER
    NEW
    PYTHON3
```
