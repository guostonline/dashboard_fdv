import streamlit as st
from src.send_image import SendImage
import plotly.express as px
from src.myEnum import Famille, Categorie, Extra,CatFamille
from src.excel_fonctions import Excel
from src.fdv import *
from src.famille import *
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

select_categorie_famille=st.sidebar.selectbox("Categories de famille",options=[catFamille.value for catFamille in CatFamille])
select_famille = st.sidebar.multiselect(
    "Select Famille",
    get_famille_by_categorie(select_categorie_famille),
    default=get_famille_by_categorie(select_categorie_famille),
    
)
options_extra = st.sidebar.selectbox("Extra", [hScore.value for hScore in Extra])
suivi = Suivi(
    st.session_state.total_days_month, st.session_state.days_worked, real_days_rest
)
df_table,df_chart = suivi.df_filter(select_vendeur, select_famille)
#df_chart = suivi.filter_vendeur_famille(select_vendeur, select_famille)

df_whatsapp=suivi.df_for_whatsapp(select_vendeur, select_famille)
print(st.session_state.total_days_month, st.session_state.days_worked, real_days_rest)


st.dataframe(df_table)
send_image=SendImage(df_whatsapp,select_vendeur)

st.button("Send images",on_click=send_image.send_image)
vendeur_ca = (
    df_chart.groupby(by=["Vendeur"]).sum()[["REAL", "OBJ"]].sort_values(by="REAL")
)

graph_bar = px.bar(
    vendeur_ca, 
    y=vendeur_ca.index,
    x=["OBJ","REAL"], 
    title="Real vs OBJ",
    barmode='group',
    height=550,
    width=500,
    )
 


st.plotly_chart(graph_bar)
