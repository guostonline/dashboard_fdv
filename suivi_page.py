
import pandas as pd
#import gspread
import streamlit as st

import pip
pip.main(["install", "gspread"])

from src.excel_fonctions import Excel


def suivi_page() :
    if "load_state" not in st.session_state:
        st.session_state.load_state = True
    uploaded_file = st.sidebar.file_uploader(
        "Choisir un fichier excel.",
        type="xlsx",
    )
    if uploaded_file is not None and st.session_state.load_state:
        sheet = Excel(uploaded_file)
        sheet.fix_sheet()
        df=pd.read_excel("excel/finale.xlsx")
        
        st.write(df)
        


def update_sheet():
    pass


   
    
st.button("Update", on_click=update_sheet)  