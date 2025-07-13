import streamlit as st
import openai

# Tajný klíč se načítá ze streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="AI Health Advisor", page_icon="🧠")
st.title("🧠 AI Personal Health Advisor")

st.markdown("Zadej svá data a získej doporučení pro zdravější den.")

sleep = st.slider("🛌 Spánek (v hodinách)", 0, 12, 7)
mood = st.text_input("😊 Jak se dnes cítíš?", "Jsem trochu unavená, ale v pohodě.")
heart = st.slider("❤️ Klidový srdeční tep (BPM)", 40, 120, 70)
coffee = st.slider("☕ Počet káv dnes", 0, 10, 2)
steps = st.slider("🚶‍♀️ Počet kroků", 0, 30000, 5000)

if st.button("📋 Generuj doporučení"):
    prompt = f"""
Uživatelská data:
- Spánek: {sleep} h
- Nálada: {mood}
- Srdeční tep: {heart} BPM
- Kávy: {coffee}
- Kroky: {steps}

Napiš 3 personalizované rady pro zlepšení fyzického i mentálního stavu dnes.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    st.subheader("🩺 Doporučení pro dnešek:")
    st.write(response.choices[0].message["content"])
