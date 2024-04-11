import streamlit as st

# Функция для отображения информации о члене команды
def display_member(name, photo, telegram_url, github_url, website_url):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(photo, width=150)
    with col2:
        st.markdown(f"#### {name}")
        st.markdown(f"[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)]({telegram_url}) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)]({github_url}) [![Website](https://img.shields.io/badge/Website-0A0A0A?style=for-the-badge&logo=google-chrome&logoColor=white)]({website_url})")

# Заголовок страницы
st.title('Наша Команда')

# Информация о членах команды
members = [
    {
        "name": "Михаил ",
        "photo": "pics/ml.png",  # Укажите путь к фотографии
        "telegram_url": "https://t.me/Mikhail_Bykov",
        "github_url": "https://github.com/username1",
        "website_url": " "
    },
    {
        "name": "Давид",
        "photo": "pics/ml.png",  # Укажите путь к фотографии
        "telegram_url": "https://t.me/nonGilgamesh",
        "github_url": "https://github.com/all-mute",
        "website_url": "https://merkulov.ai"
    },
    {
        "name": "Глеб",
        "photo": "pics/ml.png",  # Укажите путь к фотографии
        "telegram_url": "https://t.me/Glebeshye",
        "github_url": "https://github.com/Glebexe",
        "website_url": "https://github.com/Glebexe"
    }
]

# Отображение информации о каждом члене команды
for member in members:
    display_member(member["name"], member["photo"], member["telegram_url"], member["github_url"], member["website_url"])
    st.markdown("---")
