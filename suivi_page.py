import streamlit as st
from datetime import date
from src.database.database import SaveSuivi
from src.vendeurs_phone import *


is_upload = False
today = date.today().strftime("%d/%m/%Y")
def suivi_page():
    upload_file = st.sidebar.file_uploader("upload Excel file", "xlsx")
    
    


    def add_to_database(date: str):
      
        suivi = SaveSuivi(upload_file,date)
        suivi.send_all_vendeurs()


    if upload_file is not None:
        is_upload = True
    date_text=st.date_input("choisir une date",date.today(),format="DD/MM/YYYY")
   
    send_data = st.button("Send Date")
    if send_data and date_text is not None:
        add_to_database(date_text)
