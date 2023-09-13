import streamlit as st
import pandas as pd
from src.myEnum import Famille, Categorie, Extra
from src.excel_fonctions import Excel
from src.fdv import *
from src.suivi import Suivi


st.set_page_config(page_title="Rapport FDV", page_icon=":bar_chart:", layout="wide")
get_day_work = 24

if "total_days_month" not in st.session_state:
    st.session_state.total_days_month = (24,)
if "days_worked" not in st.session_state:
    st.session_state.days_worked = (1,)

day_work = 1
real_days_rest = 1


if "load_state" not in st.session_state:
    st.session_state.load_state = True






uploaded_file = st.sidebar.file_uploader(
    "Choisir un fichier excel.",
    type="xlsx",
)


if uploaded_file is not None and st.session_state.load_state:
    sheet = Excel(uploaded_file)
    sheet.fix_sheet()
    sheet.get_day_work()
    (
        st.session_state.days_worked,
        st.session_state.total_days_month,
    ) = sheet.get_day_work()
    st.session_state.load_state = False
real_days_rest = st.sidebar.number_input("Real days rest", min_value=1, max_value=26)


st.sidebar.text(
    f"Days works: {st.session_state.days_worked}/{st.session_state.total_days_month}"
)


categories = st.sidebar.selectbox(
    "Categories", [categorie.value for categorie in Categorie]
)

select_vendeur = st.sidebar.multiselect(
    "Select FDV", options=get_categorie(categories), default=get_categorie(categories)
)


select_famille = st.sidebar.multiselect(
    "Select Famille",
    [famille.value for famille in Famille],
    default="C.A (ht)",
    
)
options_extra = st.sidebar.selectbox("Extra", [hScore.value for hScore in Extra])
suivi = Suivi(
    st.session_state.total_days_month, st.session_state.days_worked, real_days_rest
)
df = suivi.filter_vendeur_famille(select_vendeur, select_famille)
print(st.session_state.total_days_month, st.session_state.days_worked, real_days_rest)
# df_mod = df.query("Famille==@select_famille & Vendeur==@select_vendeur")

st.dataframe(df)
