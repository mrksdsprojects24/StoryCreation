import streamlit as st
from transformers import pipeline

# Choose the model name (replace if needed)
model_name = "ajibawa-2023/Young-Children-Storyteller-Mistral-7B"

# Load the text-generation pipeline
generator = pipeline("text-generation", model=model_name)

st.title("Young Children's Storyteller")

# Prompt input field
prompt = st.text_input("Enter a starting phrase or keyword (optional)", "")

# Generate button
if st.button("Generate Story"):
  # Generate text with the prompt and maximum length
  generated_text = generator(prompt, max_length=500, do_sample=True)[0]['generated_text']
  st.write(generated_text)
  