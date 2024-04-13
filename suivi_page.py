
import pandas as pd
#import gspread
import streamlit as st



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
        
    date=st.date_input(label="Date")


    click_me=st.button("Add data")
    if click_me:
        df=df.astype(
           { "J-1":"int"}
        )
        j_1_list = df["J-1"].tolist()
        j_1_list = [int(x) for x in j_1_list]
        j_1_list.insert(0, date)
        Excel.add_data_to_database(j_1_list)
        st.info("success")
    
            
   
    
