from src.database.database import SaveSuivi
from src.vendeurs_phone import *
vendeurs:list=list(vendeur_number_phone.keys())
print(vendeurs)
suivi=SaveSuivi(vendeurs,"suivi.xlsx")
#suivi.send_all_vendeurs()
suivi.find_vendeur("K91 BAIZ MOHAMED")
