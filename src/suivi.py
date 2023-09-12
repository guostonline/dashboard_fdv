import pandas as pd
import numpy as np
from src.myEnum import Extra


class Suivi:
    days_towork=0
    worked_days=0
    real_days_rest=0
    def __init__(self,) -> None:
        
        self.df = pd.read_excel("excel/finale.xlsx")
        list_of_string_H: list = self.df[self.df["H"].apply(lambda x: isinstance(x, str))]

        for i in list_of_string_H.index:
            self.df.loc[i, "H"] = 0
        self.df = self.df.astype(
            {
                "REAL": "int",
                "OBJ": "int",
                "EnCours": "int",
                "Real 2023": "int",
                "Historique 2022": "int",
            }
        )
       
        
        #self.df["OBJ ttc"] = self.df.OBJ.apply(lambda x: (x * (self.df["OBJ"]*(days_towork/worked_days) ))* 1.2)
        self.df["REAL"]=self.df["REAL"]+self.df["EnCours"]
        self.df["Percent"]=self.df["REAL"]/self.df["OBJ"]-1
        self.df.loc[:, "Percent"] = self.df["Percent"].map("{:.1%}".format)

        self.df.loc[:, "H"] = self.df["H"].map("{:.1%}".format)
        self.df.replace(0,1,inplace=True)
        self.df["OBJ ttc"]=round(self.df["OBJ"]*self.days_towork/self.worked_days)*1.2
        self.df['RAF']=round((self.df['OBJ ttc']-(self.df["REAL"]*1.2))/self.real_days_rest)
        
    def filter_vendeur_famille(self, vendeur: str, famille: str):
        
        df_mod = self.df.query("Famille==@famille & Vendeur==@vendeur")
        df_mod=df_mod.style.highlight_max(subset=["REAL"]).highlight_min(color="red" ,subset=["REAL"])
       

        return df_mod

    @property
    def get_all_vendeurs(self):
        all_fdv = self.df["Vendeur"].unique()
        return all_fdv
    
    
        