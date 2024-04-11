import streamlit as st
import pandas as pd

# Создаем тестовые данные для таблиц
data1 = {
    'Model': ['Eng_to_Lij_w2vpre', 'Eng_to_Mag_w2vpre', 'Eng_to_Ace_w2vpre', 'Eng_to_Dik_w2vpre',
              'Eng_to_Lij_facebook', 'Eng_to_Mag_facebook', 'Eng_to_Ace_facebook', 'Eng_to_Dik_facebook'],
    'BLUE': [2.90, 4.34, 0.5, 0.76, 9.53, 25.89, 0.71, 2.39],
    'chrf': [28.58, 28.67, 20.16, 19.86, 39.04, 56.00, 0.34, 22.26],
    'COMET': [0.463, 0.472, 0.547, 0.582, 0.579, 0.655, 0.29, 0.534]
}

# Преобразуем словари в DataFrame
df1 = pd.DataFrame(data1)
#df2 = pd.DataFrame(data2)

# Создаем вкладки для переключения между таблицами
tab1, tab2 = st.tabs(["Первая таблица"])

with tab1:
    st.write("Таблица 1")
    st.dataframe(df1)
