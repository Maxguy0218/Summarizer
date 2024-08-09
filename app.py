import streamlit as st
from transformers import pipeline

# Load the BART model for summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

st.title("Text Summarizer")

text = st.text_area("Enter the text you want to summarize:")

# Input for summary length
max_length = st.slider("Select the maximum length of the summary:", min_value=50, max_value=300, value=150, step=10)
min_length = st.slider("Select the minimum length of the summary:", min_value=10, max_value=max_length-10, value=50, step=10)

# Button to trigger summarization
if st.button("Summarize"):
    if text:
        # Perform the summarization using the BART model
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        st.subheader("Summary")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
