import streamlit as st
from streamlit_option_menu import option_menu
from src.send_image import SendImage
from datetime import date
import plotly.express as px
from millify import millify,prettify
from src.myEnum import Famille, Categorie, Extra, CatFamille
from src.excel_fonctions import Excel
from src.my_fonctions import MyFonctions
from src.fdv import *
from src.famille import *
from src.suivi import Suivi




def home_page():
    
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
    real_days_rest = st.sidebar.number_input(
        "Real days rest", min_value=1, max_value=26
    )

    st.sidebar.text(
        f"Days works: {st.session_state.days_worked}/{st.session_state.total_days_month}"
    )

    categories = st.sidebar.selectbox(
        "Categories", [categorie.value for categorie in Categorie]
    )

    select_vendeur = st.sidebar.multiselect(
        "Select FDV",
        options=get_categorie(categories),
        default=get_categorie(categories),
    )

    select_categorie_famille = st.sidebar.selectbox(
        "Categories de famille", options=[catFamille.value for catFamille in CatFamille]
    )
    select_famille = st.sidebar.multiselect(
        "Select Famille",
        get_famille_by_categorie(select_categorie_famille),
        default=get_famille_by_categorie(select_categorie_famille),
    )
    options_extra = st.sidebar.selectbox("Extra", [hScore.value for hScore in Extra])
    suivi = Suivi(
        st.session_state.total_days_month, st.session_state.days_worked, real_days_rest
    )
    df_table, df_chart = suivi.df_filter(select_vendeur, select_famille)

    df_whatsapp = suivi.df_for_whatsapp(select_vendeur, select_famille)
    print(
        st.session_state.total_days_month, st.session_state.days_worked, real_days_rest
    )

    col_ca, col_real, col_road_cdz1, col_road_cdz2 = st.columns(4)

    with col_ca:
        st.metric("Objective Parciale",millify(suivi.get_detail_obj_parcial(),precision=3) , f'Historique: {suivi.get_detail_historique()}%')
    with col_real:
        st.metric("Réalisation", millify(suivi.get_detail_real(),precision=3), f'Objectif: {round((suivi.get_detail_real()/suivi.get_detail_obj_parcial()-1)*100)}%')
    with col_road_cdz1:
        col_real = st.metric("Road to win cdz1", 880000, 88)
    with col_road_cdz2:
        col_real = st.metric("Road to win cdz2", 880000, 88)

    col_message, col_send_message, col_vide = st.columns(3)
    today = date.today().strftime("%d/%m/%Y")

    message = col_message.text_input("Message", value=today)

    send_image = SendImage(df_whatsapp, select_vendeur, message=message)
    today = date.today().strftime("%d/%m/%Y")

    col_send_message.button("Send images", on_click=send_image.send_image)
    vendeur_ca = (
        df_chart.groupby(by=["Vendeur"]).sum()[["REAL", "OBJ"]].sort_values(by="REAL")
    )

    def set_color() -> list:
        my_list = []
        for i in range(len(df_chart)):
            if df_chart["REAL"].values[i] >= df_chart["OBJ"].values[i]:
                my_list.append("green")

            else:
                my_list.append("red")

        return my_list

    graph_bar = px.bar(
        vendeur_ca,
        y=vendeur_ca.index,
        x=["OBJ", "REAL"],
        title="Real vs OBJ",
        barmode="group",
        height=550,
        width=500,
    )
    graph_bar_color = px.bar(
        vendeur_ca,
        y=vendeur_ca.index,
        x=["OBJ", "REAL"],
        title="Real vs OBJ",
        barmode="overlay",
        height=550,
        width=500,
        color_discrete_sequence=set_color(),
    )

    def famille_chart(famille: Famille) -> px.bar:
        chart = px.bar(
            suivi.chart_famille(famille.name, select_vendeur),
            y=suivi.chart_famille(famille.name, select_vendeur).index,
            x=["OBJ", "REAL"],
            title=famille.name,
            barmode="group",
            width=400,
            height=250,
        )
        return chart

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(graph_bar)
    with col2:
        st.plotly_chart(graph_bar_color)

    col3, col4, col5 = st.columns(3)
    with col3:
        st.plotly_chart(famille_chart(famille=Famille.LEVURE))
    with col4:
        st.plotly_chart(famille_chart(famille=Famille.FLAN))
    with col5:
        st.plotly_chart(famille_chart(famille=Famille.BOUILLON))
    col6, col7, col8 = st.columns(3)
    with col6:
        st.plotly_chart(famille_chart(famille=Famille.CONDIMENTS))
   
    with col8:
        st.plotly_chart(famille_chart(famille=Famille.CONSERVES))

    with col7:
        st.plotly_chart(famille_chart(famille=Famille.SAUCES))
    