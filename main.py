
import streamlit as st
import random

st.set_page_config(
    page_title="Мій супер додаток",
    page_icon="🐍",
    layout="wide"
)

# ДИЗАЙН САЙТУ
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }

    h1, h2, h3 {
        color: #FF8FAB;
    }

    div.stButton > button {
        background-color: #FF4B8B;
        color: white;
        border-radius: 12px;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #FF80AB;
        color: white;
    }

    .stTabs [data-baseweb="tab"] {
        color: #FAFAFA;
        font-size: 17px;
    }

    .stTabs [aria-selected="true"] {
        color: #FF8FAB;
    }
</style>
""", unsafe_allow_html=True)

st.title("Ласкаво просимо до мого додатка!")

tab1, tab2, tab3 = st.tabs([
    "Про мене",
    "Мій інструмент",
    "🔗 Корисні посилання"
])

# ПЕРША ВКЛАДКА
with tab1:
    st.header("Знайомство з автором")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("images.jpg", caption="Я", width=400)

    with col2:
        st.subheader("Привіт, я майбутній Python Developer")

        st.write(
            "Я навчаюсь в Малій Комп'ютерній Академії IT STEP. "
            "Створюю круті веб-додатки та вивчаю Streamlit."
        )

        with st.container():
            st.info("Контакти для зв'язку")

            st.markdown(
                "- GitHub: [Мій профіль](https://github.com/pugacovadiana55-commits)"
            )

            st.markdown(
                "- E-Mail: [Моя електронна пошта](mailto:pugacovadiana55@gmail.com)"
            )


# ДРУГА ВКЛАДКА — ГРА
with tab2:
    st.header("🎲 Гра «Вгадай число»")

    st.write(
        "Я загадав число від 1 до 100. "
        "Спробуй його вгадати!"
    )

    # Створюємо число тільки на початку гри
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)

    if "attempts" not in st.session_state:
        st.session_state.attempts = 0

    if "game_over" not in st.session_state:
        st.session_state.game_over = False

    if "message" not in st.session_state:
        st.session_state.message = ""

    # Поле для введення числа
    guess = st.number_input(
        "Введи своє число:",
        min_value=1,
        max_value=100,
        value=1,
        step=1
    )

    # Перевірка числа
    if st.button(
        "Перевірити",
        disabled=st.session_state.game_over
    ):
        st.session_state.attempts += 1

        if guess < st.session_state.secret_number:
            st.session_state.message = "📈 Моє число більше!"

        elif guess > st.session_state.secret_number:
            st.session_state.message = "📉 Моє число менше!"

        else:
            st.session_state.message = "🎉 Вітаю! Ти вгадав число!"
            st.session_state.game_over = True
            st.balloons()

    if st.session_state.message:
        if st.session_state.game_over:
            st.success(st.session_state.message)
        else:
            st.info(st.session_state.message)

    st.write(
        f"Кількість спроб: {st.session_state.attempts}"
    )

    # Почати нову гру
    if st.button("🔄 Нова гра"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.message = ""
        st.rerun()


# ТРЕТЯ ВКЛАДКА
with tab3:
    st.header("🔗 Корисні посилання")

    st.write("Мої улюблені сайти для навчання та розваг!")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("📚 Навчання")

        st.markdown(
            "🐍 [Вивчення Python](https://www.w3schools.com/python/)"
        )

        st.markdown(
            "💻 [Документація Streamlit](https://docs.streamlit.io/)"
        )

    with col4:
        st.subheader("🎮 Ігри та творчість")

        st.markdown(
            "🐱 [Scratch](https://scratch.mit.edu/)"
        )

        st.markdown(
            "🧩 [Code.org](https://code.org/)"
        )
