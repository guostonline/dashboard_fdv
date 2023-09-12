import streamlit as st
import pandas as pd
from src.myEnum import Famille, Categorie, Extra
from src.excel_fonctions import Excel
from src.fdv import *
from src.suivi import Suivi


st.set_page_config(page_title="Rapport FDV", page_icon=":bar_chart:", layout="wide")
get_day_work = 24
total_days_month, days_worked = 24, 1
day_work = 1
real_days_rest = 1
uploaded_file = st.sidebar.file_uploader(
    "Choisir un fichier excel.",
    type="xlsx",
)

if uploaded_file is not None:
    sheet = Excel(uploaded_file)
    sheet.fix_sheet()
    sheet.get_day_work()
    days_worked, total_days_month = sheet.get_day_work()
suivi = Suivi()

st.sidebar.text(f"Days works: {days_worked}/{total_days_month}")
real_days_rest = st.sidebar.number_input("Real days rest", min_value=1, max_value=26)
suivi.real_days_rest = real_days_rest
suivi.days_towork = total_days_month
suivi.worked_days = days_worked

categories = st.sidebar.selectbox(
    "Categories", [categorie.value for categorie in Categorie]
)

select_vendeur = st.sidebar.multiselect(
    "Select FDV", options=get_categorie(categories), default=get_categorie(categories)
)


select_famille = st.sidebar.multiselect(
    "Select Famille",
    [famille.value for famille in Famille],
    default='C.A (ht)'
)
options_extra = st.sidebar.selectbox("Extra", [hScore.value for hScore in Extra])
df = suivi.filter_vendeur_famille(select_vendeur, select_famille)

# df_mod = df.query("Famille==@select_famille & Vendeur==@select_vendeur")

st.dataframe(df)
