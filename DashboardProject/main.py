import streamlit as st
import sys
from dbutils.pooled_db import PooledDB
import pymysql
from src.movies_count import plot_movies
from src.countries_count import plot_countries

HOST = sys.argv[1]
PORT = int(sys.argv[2])
USER = sys.argv[3]
PASSWORD = sys.argv[4]


def my_dashboard(cur):
    """
    Лэйаут дешборда
    """
    st.set_page_config(
    layout="wide",
    page_title="ChartsAreCool",
    initial_sidebar_state="expanded"
    )
    st.markdown("<h1 style='text-align:center '>Let's explore your data! 🌅</h1>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Movies Stats", "Companies' Countries"])
    with tab1:
        year_start = st.number_input('Enter  the starting year (2000 by default)', value=2000)
        if year_start:
            st.plotly_chart(plot_movies(cur, year_start), theme="streamlit", use_container_width=True)
    with tab2:
        n_out = st.number_input('Enter max number of countries (10 by default)', value=10)
        if n_out:
            st.plotly_chart(plot_countries(cur, n_out))


def start_process():
    # подключение к базе данных MySQL
    pool = PooledDB(pymysql, host=HOST, user=USER,
                    passwd=PASSWORD, db="mydash", port=PORT,
                    charset="utf8", cursorclass=pymysql.cursors.SSCursor)
    conn = pool.connection()
    cur = conn.cursor()
    my_dashboard(cur)


if __name__ == '__main__':
    start_process()
