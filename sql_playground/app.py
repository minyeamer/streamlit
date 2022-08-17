import streamlit as st
import pandas as pd
import webbrowser

# DB Mgmt
import sqlite3
conn = sqlite3.connect("data/world.sqlite", check_same_thread=False)
cursor = conn.cursor()

def sql_executor(raw_code):
    cursor.execute(raw_code)
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    return data, columns

city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']
country = ['Code,', 'Name,', 'Continent,', 'Region,', 'SurfaceArea,', 'IndepYear,', 'Population,', 'LifeExpectancy,', 'GNP,', 'GNPOld,', 'LocalName,', 'GovernmentForm,', 'HeadOfState,', 'Capital,', 'Code2']
countrylanguage = ['CountryCode,', 'Language,', 'IsOfficial,', 'Percentage']

def main():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    st.title("SQLPlayground")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("HomePage")
        
        # Columns/Layout 
        col1, col2 = st.columns(2)
        with col1:
            with st.form(key="query_form"):
                raw_code = st.text_area("SQL Code Here")
                submit_code = st.form_submit_button("Execute")

            # Table of Info
            with st.expander("Table Info"):
                t_info = {'city' : city, 'country' : country, 'countrylanguage' : countrylanguage}
                st.json(t_info)

        # Result Layouts
        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)

                # Results 
                query_results, columns = sql_executor(raw_code)
                with st.expander("Results"):
                    st.write(query_results)

                with st.expander("Pretty Table"):
                    query_df = pd.DataFrame(query_results, columns=columns)
                    st._legacy_dataframe(query_df)
            else:
                st.info("Query Required")

    elif choice == "About":
        st.subheader("Reference")
        if st.button("Github link"):
            webbrowser.open_new_tab("https://github.com/minyeamer/streamlit")
        if st.button("Original source"):
            webbrowser.open_new_tab("https://github.com/Jcharis/Streamlit_DataScience_Apps")

if __name__ == "__main__":
    main()