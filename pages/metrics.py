for i, tab in enumerate(tabs):
    with tab:
        # Фильтруем DataFrame по языку
        filtered_df = df[df['Model'].str.contains(tab_labels[i])]

        # Выбираем только числовые столбцы для вычисления разницы
        numeric_columns = filtered_df.select_dtypes(include=[np.number])

        if len(filtered_df) == 2:  # Убедимся, что есть ровно две модели для сравнения
            # Вычисляем разницу только для числовых столбцов
            diff_values = numeric_columns.diff().iloc[-1]  # Разница в значениях
            diff_percents = numeric_columns.pct_change().iloc[-1] * 100  # Разница в процентах

            # Создаем DataFrame для разницы
            diff_df = pd.DataFrame([diff_values, diff_percents], index=['Разница', 'Разница (%)']).rename(
                columns=lambda x: filtered_df.columns[x + 1])

            # Добавляем название модели обратно для удобства отображения
            model_names = filtered_df['Model'].reset_index(drop=True)
            diff_df.insert(0, 'Model', ['Разница', 'Разница (%)'])

            # Транспонируем отфильтрованный DataFrame, исключая столбец 'Model'
            df_transposed = filtered_df.drop('Model', axis=1).T

            # Объединяем транспонированный DataFrame с DataFrame разницы
            result_df = pd.concat([df_transposed, diff_df])

            st.write(f"Сравнение моделей для {tab_names[i]} по метрикам, включая разницу в значениях и процентах")
            st.dataframe(result_df)
        else:
            st.write("Для сравнения должно быть ровно две модели.")
