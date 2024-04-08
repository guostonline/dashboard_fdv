categories_famille_som: list[str] = [
    "LEVURE",
    "FLAN",
    "BOUILLON",
    "C.A (ht)",
]
categories_famille_vmm: list[str] = [
    "CONDIMENTS",
    "SAUCES",
    "CONSERVES",
    "C.A (ht)",
]
categories_famille_all: list[str] = [
    "LEVURE",
    "FLAN",
    "BOUILLON",
    "CONDIMENTS",
    "SAUCES",
    "CONSERVES",
    "C.A (ht)",
]

def get_famille_by_categorie(categorie:str)->list:
    if categorie=="SOM":
        return categories_famille_som
    elif categorie=="VMM":
        return categories_famille_vmm
    elif categorie=="ALL":
        return categories_famille_all