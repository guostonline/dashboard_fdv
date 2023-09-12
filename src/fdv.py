pre_vendeur: list = [
    "Y59 EL GHANMI MOHAMED",
    "F77 EL MEZRAOUI YOUSSEF",
    "T45 FAICAL GOUIZID",
    "E31 BENCHOUIKH MOHAMMED",
    "D45 OUARSSASSA YASSINE",
    "Y60 ATOUAOU AIMAD",
    "E66 MOUTAOUAKIL MOSTAFA",
    "D86 ACHAOUI AZIZ",
    "K91 BAIZ MOHAMED",
    "E14 BOUMDIANE MOHAMED",
    "F78 GHOUSMI MOURAD",
    "E60 BOUALLALI FARID",
]
som_pre_vendeur: list = [
    "Y59 EL GHANMI MOHAMED",
    "E31 BENCHOUIKH MOHAMMED",
    "D45 OUARSSASSA YASSINE",
    "D86 ACHAOUI AZIZ",
    "E14 BOUMDIANE MOHAMED",
    "F78 GHOUSMI MOURAD",
]
vmm_pre_vendeur:list=[
    "F77 EL MEZRAOUI YOUSSEF",
    "T45 FAICAL GOUIZID",
    "Y60 ATOUAOU AIMAD",
    "E66 MOUTAOUAKIL MOSTAFA",
    "K91 BAIZ MOHAMED",
    "E60 BOUALLALI FARID",
]
som_all: list = [
    "Y59 EL GHANMI MOHAMED",
    "E31 BENCHOUIKH MOHAMMED",
    "D45 OUARSSASSA YASSINE",
    "D86 ACHAOUI AZIZ",
    "E14 BOUMDIANE MOHAMED",
    "F78 GHOUSMI MOURAD",
    "485 NAMOUSS ABDESSAMAD",
    "F82 AKKA ABDESSLAM",
    "E18 BOUBRIK MOHAMED",
    "T89 AKNOUN MOHAMED",
    "K60 ELHAOUZI RACHID",
    "D48 IBACH MOHAMED",
]
vmm_all:list=[
    "F77 EL MEZRAOUI YOUSSEF",
    "T45 FAICAL GOUIZID",
    "Y60 ATOUAOU AIMAD",
    "E66 MOUTAOUAKIL MOSTAFA",
    "K91 BAIZ MOHAMED",
    "E60 BOUALLALI FARID",
    "485 NAMOUSS ABDESSAMAD",
    "F82 AKKA ABDESSLAM",
    "E18 BOUBRIK MOHAMED",
    "T89 AKNOUN MOHAMED",
    "K60 ELHAOUZI RACHID",
    "D48 IBACH MOHAMED",
]
conventionnel: list = [
    "485 NAMOUSS ABDESSAMAD",
    "F82 AKKA ABDESSLAM",
    "E18 BOUBRIK MOHAMED",
    "T89 AKNOUN MOHAMED",
    "K60 ELHAOUZI RACHID",
    "D48 IBACH MOHAMED",
]


def get_categorie(categories: str):
    if categories == "Pré-vendeur":
        return pre_vendeur
    elif categories == "Conventionnel":
        return conventionnel
    elif categories == "One by One":
        return pre_vendeur[0]
    elif categories == "SOM pré-vendeur":
        return som_pre_vendeur
    elif categories == "VMM pré-vendeur":
        return vmm_pre_vendeur
    elif categories == "SOM All":
        return som_all
    elif categories == "VMM All":
        return vmm_all
    return pre_vendeur + conventionnel
