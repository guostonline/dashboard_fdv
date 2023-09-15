from enum import Enum


class Famille(Enum):
    LEVURE = "LEVURE"
    COLORANT = "COLORANT"
    BOUILLON = "BOUILLON"
    CONDIMENTS = "CONDIMENTS"
    SAUCE = "SAUCES TACOS"
    CONSERVES = "CONSERVES"
    CA = "C.A (ht)"


class Categorie(Enum):
    PREVENDEUR = "Pré-vendeur"
    CONVENTIONNEL = "Conventionnel"
    ALLFDV = "ALL FDV"
    SOMPREVENTE = "SOM pré-vendeur"
    VMMPREVENTE = "VMM pré-vendeur"
    SOMALL = "SOM All"
    VMMALL = "VMM All"
    ONEBYONE = "One by One"


class Extra(Enum):
    HIGHTSCORE = "Hight Score"
    SMALLSCORE = "Smal Score"


class CatFamille(Enum):
    ALL = "ALL"
    SOM = "SOM"
    VMM = "VMM"
