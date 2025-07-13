import streamlit as st
from openai import OpenAI
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Health Advisor", layout="wide")

client = OpenAI()

def get_health_advice(prompt: str, category: str) -> str:
    system_msg = f"Jsi zkušený zdravotní asistent specializovaný na {category}."
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Chyba při volání OpenAI API: {e}"

def plot_sleep_quality():
    days = ["Po", "Út", "St", "Čt", "Pá", "So", "Ne"]
    hours = [7, 6.5, 8, 7.5, 6, 7, 8]
    plt.figure(figsize=(8,3))
    plt.plot(days, hours, marker='o', linestyle='-', color='purple')
    plt.title("Kvalita spánku (hodiny za noc)")
    plt.ylim(5,9)
    plt.grid(True)
    st.pyplot(plt)

st.title("🧠 AI Personal Health Advisor")

# Výběr kategorie doporučení
category = st.radio(
    "Vyber kategorii doporučení:",
    ("obecné", "výživa", "cvičení", "spánek"),
    horizontal=True
)

col1, col2 = st.columns([3,2])

with col1:
    user_input = st.text_area("Napiš svůj dotaz:")

    if st.button("🔍 Generuj doporučení"):
        if user_input.strip() == "":
            st.warning("⚠️ Prosím, zadej svůj dotaz.")
        else:
            with st.spinner("🧬 Generuji doporučení..."):
                advice = get_health_advice(user_input, category)
            st.success("✅ Hotovo!")
            st.write(advice)

            # Ulož historii do session state
            if "history" not in st.session_state:
                st.session_state.history = []
            st.session_state.history.append((user_input, advice))

with col2:
    st.markdown("### 📊 Ukázkový graf spánku")
    plot_sleep_quality()

    if "history" in st.session_state and st.session_state.history:
        st.markdown("### 🕘 Historie tvých dotazů")
        for i, (q, a) in enumerate(reversed(st.session_state.history[-5:]), 1):
            st.markdown(f"**Dotaz {i}:** {q}")
            st.markdown(f"**Doporučení:** {a}")
            st.write("---")
