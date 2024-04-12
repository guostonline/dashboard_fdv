import streamlit as st
from streamlit_option_menu import option_menu
from home import *
from suivi_page import suivi_page



st.set_page_config(page_title="Rapport FDV", page_icon=":bar_chart:", layout="wide")

with st.sidebar:
    global selected
    selected = option_menu("Main Menu", ["Home", 'Add'], 
        icons=['house', 'bi-database-fill-add'], menu_icon="cast", default_index=0)
if selected=="Home":
        home_page()
if selected=="Adds":  
        suivi_page()

