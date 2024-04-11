import streamlit as st
import pandas as pd

# Создаем отдельные DataFrame для каждого языка
data_li = {
    'Model': ['Eng_to_Lij_w2vpre', 'Eng_to_Lij_facebook'],
    'BLUE': [2.90, 9.53],
    'chrf': [28.58, 39.04],
    'COMET': [0.463, 0.579]
}

data_mag = {
    'Model': ['Eng_to_Mag_w2vpre', 'Eng_to_Mag_facebook'],
    'BLUE': [4.34, 25.89],
    'chrf': [28.67, 56.00],
    'COMET': [0.472, 0.655]
}

data_ace = {
    'Model': ['Eng_to_Ace_w2vpre', 'Eng_to_Ace_facebook'],
    'BLUE': [0.5, 0.71],
    'chrf': [20.16, 0.34],
    'COMET': [0.547, 0.29]
}

data_dik = {
    'Model': ['Eng_to_Dik_w2vpre', 'Eng_to_Dik_facebook'],
    'BLUE': [0.76, 2.39],
    'chrf': [19.86, 22.26],
    'COMET': [0.582, 0.534]
}

dfs = {
    "Язык Lij": pd.DataFrame(data_li),
    "Язык Mag": pd.DataFrame(data_mag),
    "Язык Ace": pd.DataFrame(data_ace),
    "Язык Dik": pd.DataFrame(data_dik)
}

# Функция для добавления строки с процентной разницей между моделями
def add_percentage_difference_row(df):
    percentage_diff = {}
    # Предполагаем, что у нас всегда две модели для сравнения
    for metric in ['BLUE', 'chrf', 'COMET']:
        if df[metric][0] != 0:  # Избегаем деления на ноль
            percentage_diff[metric] = ((df[metric][1] - df[metric][0]) / df[metric][0]) * 100
        else:
            percentage_diff[metric] = float('inf')  # Если первое значение равно нулю, ставим бесконечность
    # Создаем строку с процентными разницами
    diff_row = ['Facebook лучше на:', percentage_diff['BLUE'], percentage_diff['chrf'], percentage_diff['COMET']]
    # Добавляем строку в DataFrame
    df.loc[len(df)] = diff_row
    return df

# Применяем функцию к каждому DataFrame
for lang, df in dfs.items():
    dfs[lang] = add_percentage_difference_row(df)

# Создаем вкладки для каждого языка
tab_names = list(dfs.keys())
tabs = st.tabs(tab_names)

for tab_name, tab in zip(tab_names, tabs):
    with tab:
        st.write(f"Сравнение моделей для {tab_name} по метрикам")
        st.dataframe(dfs[tab_name])
