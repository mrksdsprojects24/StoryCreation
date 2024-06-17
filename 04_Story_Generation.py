import streamlit as st
from transformers import pipeline

st.title("Krishna's Story Generation App")

tg_pipeline = pipeline("text-generation", model="gpt2")

# User input field for text
text = st.text_input("Enter a few details for me to write a story around and click 'Generate' button.")

# Button to trigger summarization
if st.button("Generate"):
  prompt = f"Let us write a story. {text}."
  story = tg_pipeline(
    prompt,
    pad_token_id=tg_pipeline.tokenizer.eos_token_id,
    max_new_tokens=500
  )
  st.success("Story:")
  st.write(story[0]['generated_text'])
