import streamlit as st
from transformers import pipeline

# Supported Genres (update as needed)
genres = ["adventure", "romance", "fantasy", "mystery"]

# Choose the desired model name (replace with your choice)
model_name = "aspis/gpt2-genre-story-generation" 
#                                      or "gpt2" or "facebook/bart-base"

generator = pipeline("text-generation", model=model_name)


def generate_story(genre, starting_words, temperature):
  """
  Generates story using the specified parameters.

  Args:
      genre (str): Genre for the story.
      starting_words (str, optional): Starting words for the story. Defaults to None.
      temperature (float): Sampling temperature (0.5 to 2.0).

  Returns:
      str: The generated story (complete sentence).
  """

  # For aspis/gpt2-genre-story-generation model, include genre token in prompt.
  if model_name == "aspis/gpt2-genre-story-generation":
      prompt = f"<BOS> <{genre}>"
  else:
      prompt = ""

  # Add starting words if provided
  if starting_words:
      prompt += f" {starting_words}"

  generated_text = generator(prompt, max_length=500, do_sample=True, temperature=temperature)[0]['generated_text']

  # Split the generated text into words and find the last complete sentence
  words = generated_text.split()
  last_complete_sentence_end = 0
  for i, word in enumerate(words):
    if word.endswith(".") or word.endswith("?") or word.endswith("!"):
      last_complete_sentence_end = i + 1  # Include the ending punctuation

  # Return the complete story excluding the incomplete sentence
  return " ".join(words[:last_complete_sentence_end])


st.title("Story Generator")

# Genre selection dropdown
selected_genre = st.selectbox("Genre", genres)

# Starting words input (optional)
starting_words = st.text_input("Starting Words (Optional)", "")

# Temperature slider
temperature = st.slider("Temperature (Controls Creativity)", 0.5, 2.0, value=1.0)

# Generate button
if st.button("Generate Story"):
  # Generate story and exclude incomplete sentence
  generated_story = generate_story(selected_genre, starting_words, temperature)
  st.write(generated_story)
  
