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

# Транспонируем DataFrame, чтобы модели были в строках, а метрики - в столбцах
df_transposed = df.set_index('Model').T

# Создаем вкладки для каждого языка
tab_labels = ["Lij", "Mag", "Ace", "Dik"]
tabs = st.tabs(tab_labels)

for i, tab in enumerate(tabs):
    with tab:
        # Предполагаем, что каждая модель относится к определенному языку
        # Здесь вы можете добавить фильтрацию или другую логику, чтобы отобразить данные специфично для каждого языка
        st.write(f"Сравнение моделей для языка {tab_labels[i]} по метрикам")
        st.dataframe(df_transposed)

# Обратите внимание, что вам может потребоваться адаптировать логику отображения данных в зависимости от того,
# как именно ваши данные должны быть разделены по языкам.
