import streamlit as st
import pandas as pd

# Создаем тестовые данные для таблиц
data = {
    'Model': ['Eng_to_Lij_w2vpre', 'Eng_to_Mag_w2vpre', 'Eng_to_Ace_w2vpre', 'Eng_to_Dik_w2vpre',
              'Eng_to_Lij_facebook', 'Eng_to_Mag_facebook', 'Eng_to_Ace_facebook', 'Eng_to_Dik_facebook'],
    'BLUE': [2.90, 4.34, 0.5, 0.76, 9.53, 25.89, 0.71, 2.39],
    'chrf': [28.58, 28.67, 20.16, 19.86, 39.04, 56.00, 0.34, 22.26],
    'COMET': [0.463, 0.472, 0.547, 0.582, 0.579, 0.655, 0.29, 0.534]
}

# Преобразуем словарь в DataFrame
df = pd.DataFrame(data)

# Создаем вкладки для каждого языка с более красивыми названиями
tab_labels = ["Lij", "Mag", "Ace", "Dik"]
tab_names = ["Язык Lij", "Язык Mag", "Язык Ace", "Язык Dik"]
tabs = st.tabs(tab_names)

for i, tab in enumerate(tabs):
    with tab:
        # Фильтруем DataFrame по языку
        filtered_df = df[df['Model'].str.contains(tab_labels[i])]

        # Транспонируем отфильтрованный DataFrame, чтобы модели были в строках, а метрики - в столбцах
        df_transposed = filtered_df.set_index('Model').T

        st.write(f"Сравнение моделей для {tab_names[i]} по метрикам")
        st.dataframe(df_transposed)
