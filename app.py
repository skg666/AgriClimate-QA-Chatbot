import streamlit as st
import pandas as pd

st.title("🌾 AgriClimate-QA Chatbot")
st.write("Ask questions about India's agriculture and climate data (powered by data.gov.in).")

st.write("🤖 Example questions:")
st.write("- Compare rainfall in Bihar and UP")
st.write("- Top crops in Maharashtra")

question = st.text_input("💬 Ask your question:")

if "rainfall" in question.lower():
    st.write("Average rainfall in Bihar = 980 mm, UP = 820 mm (sample data).")

elif "crop" in question.lower():
    st.write("Top crops in Maharashtra: Sugarcane, Cotton, Soybean.")

else:
    st.write("Sorry, I can currently answer only rainfall or crop questions.")
