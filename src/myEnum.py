from enum import Enum


class Famille(Enum):
    LEVURE = "LEVURE"
    FLAN = "FLAN"
    BOUILLON = "BOUILLON"
    CONDIMENTS = "CONDIMENTS"
    SAUCES = "SAUCES"
    CONSERVES = "CONSERVES"
    CA = "C.A (ht)"


class Categorie(Enum):
    CDZ="CDZ"
    PREVENDEUR = "Pré-vendeur"
    PREVENDEURCHAKIB = "Pré-vendeur Chakib"
    CONVENTIONNEL = "Conventionnel"
    ALLFDV = "ALL FDV"
    SOMPREVENTE = "SOM pré-vendeur"
    SOMPREVENTECHAKIB="SOM pré-vendeur Chakib"
    VMMPREVENTECHAKIB = "VMM pré-vendeur Chakib"
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
