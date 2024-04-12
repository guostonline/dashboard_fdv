import pandas as pd
import numpy as np
from src.myEnum import Extra, Famille
from src.my_fonctions import MyFonctions

class Suivi:
    def __init__(self, days_towork, worked_days, real_days_rest) -> None:
        self.days_towork = days_towork
        self.worked_days = worked_days
        self.real_days_rest = real_days_rest

        self.df = pd.read_excel("excel/finale.xlsx")
        list_of_string_H: list = self.df[
            self.df["H %"].apply(lambda x: isinstance(x, str))
        ]

        for i in list_of_string_H.index:
            self.df.loc[i, "H %"] = 0
        self.df = self.df.astype(
            {
                "REAL": "int",
                "OBJ": "int",
                "EnCours": "int",
                "REAL 2024": "int",
                "H 2023": "int",
            }
        )

        def highlight_max(s):
            if s.dtype == np.object:
                is_neg = [False for _ in range(s.shape[0])]
            else:
                is_neg = s < 0
            return ["color: red;" if cell else "color:black" for cell in is_neg]

        # self.df["OBJ ttc"] = self.df.OBJ.apply(lambda x: (x * (self.df["OBJ"]*(days_towork/worked_days) ))* 1.2)
        # self.df["Percent"]=self.df["Percent"].style.apply(highlight_max)
        self.df["REAL"] = self.df["REAL"] + self.df["EnCours"]
        self.df["Percent"] = self.df["REAL"] / self.df["OBJ"] - 1

        self.df.loc[:, "Percent"] = self.df["Percent"].map("{:.1%}".format)

        self.df.loc[:, "H %"] = self.df["H %"].map("{:.1%}".format)
        self.df.replace(0, 1, inplace=True)
        self.df.replace(1, 0, inplace=True)
        self.df.replace("SAUCES TACOS", "SAUCES_TACOS", inplace=True)

        self.df["OBJ ttc"] = round(
            (self.df["OBJ"] * self.days_towork / self.worked_days) * 1.2
        )

        self.df["RAF"] = (
            self.df["OBJ ttc"] - (self.df["REAL"] * 1.2)
        ) / self.real_days_rest

        self.df["Total Rest"] = round(self.df["OBJ ttc"] - (self.df["REAL"] * 1.2))
        self.df["Total Rest %"] = round(
            ((self.df["REAL"] * 1.2) / self.df["OBJ ttc"]) * 100
        )
        self.df["+110%"] = round((self.df["OBJ ttc"] * 1.1) - (self.df["REAL"] * 1.2))
        self.df["97%"] = round((self.df["OBJ ttc"] * 0.97) - (self.df["REAL"] * 1.2))
        self.df["91%"] = round((self.df["OBJ ttc"] * 0.91) - (self.df["REAL"] * 1.2))
        self.df["71%"] = round((self.df["OBJ ttc"] * 0.71) - (self.df["REAL"] * 1.2))

        self.df = self.df.astype(
            {
                "OBJ ttc": "int",
                "RAF": "int",
                "Total Rest": "int",
                "+110%": "int",
                "97%": "int",
                "91%": "int",
                "71%": "int",
            }
        )

    def df_for_whatsapp(self, vendeur: str, famille: str):
        df = self.df.query("Famille==@famille & Vendeur==@vendeur")
        return df

    def df_filter(self, vendeur: str, famille: str):
        df_mod = self.df.query("Famille==@famille & Vendeur==@vendeur")
        df = df_mod.style.set_properties(
            **{"background-color": "yellow"}, subset=["OBJ ttc", "RAF", "Total Rest"]
        )

        return df, df_mod

    def get_detail_real(self):
        df = (
            self.df.query(
                "Vendeur==['CHAKIB ELFIL','CDZ AGADIR DET2'] & Famille=='C.A (ht)'"
            )
            
            .sum()[["REAL"]]
            
        )

        return df.sum()
    
    def get_detail_obj_parcial(self):
        df = (
            self.df.query(
                "Vendeur==['CHAKIB ELFIL','CDZ AGADIR DET2'] & Famille=='C.A (ht)'"
            )
            
            .sum()[["OBJ"]]
            
        )

        return df.sum()
    def get_detail_historique(self):
        df = (
            self.df.query(
                "Vendeur==['CHAKIB ELFIL','CDZ AGADIR DET2'] & Famille=='C.A (ht)'"
            )
            .sum()[["REAL 2024"]]
            
        )
        df2 = (
            self.df.query(
                "Vendeur==['CHAKIB ELFIL','CDZ AGADIR DET2'] & Famille=='C.A (ht)'"
            )
            
            .sum()[["H 2023"]]
            
        )
        
        return round((df.sum()/df2.sum()-1)*100)
    

    @property
    def get_all_vendeurs(self):
        all_fdv = self.df["Vendeur"].unique()
        return all_fdv

    def chart_famille(self, famille: str, vendeur: str):
        df = (
            self.df.query("Famille==@famille & Vendeur==@vendeur")
            .groupby(by=["Famille"])
            .sum()[["REAL", "OBJ"]]
            .sort_values(by="REAL")
        )

        return df
