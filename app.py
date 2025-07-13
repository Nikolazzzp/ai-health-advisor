import streamlit as st
from openai import OpenAI

# Inicializace klienta
client = OpenAI()

def get_health_advice(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Jsi zdravotní asistent."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content

st.title("AI Personal Health Advisor")

user_input = st.text_area("Napiš svůj dotaz:")

if st.button("Generuj doporučení"):
    if user_input.strip() == "":
        st.warning("Prosím, zadej svůj dotaz.")
    else:
        with st.spinner("Generuji doporučení..."):
            advice = get_health_advice(user_input)
        st.success("Tady je tvoje doporučení:")
        st.write(advice)
