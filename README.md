# Text Summarizer App
This is a simple Text Summarizer App built with Python using the Streamlit library.
- **Live application** - https://para-summary.streamlit.app/

## Overview
The Text Summarizer App allows users to input text and receive a summarized version of the text, you can either upload or copy and paste text. Additionally, the app provides sentiment analysis for the entered text.
**Note**: Only pdf,docx,txt files can be uploaded for now.

## Features
- Text Summarization: The app uses natural language processing techniques to generate a concise summary of the input text.

- Sentiment Analysis: Users can perform sentiment analysis on the entered text to determine if it is positive, negative, or neutral.

## Getting Started
### Prerequisites
Python (version 3.10.13)

Install the required packages by running:
pip install -r requirements.txt


## Usage
- Enter text in the provided text area.
- Click the "Generate Summary" button to get a summarized version of the text.
- Optionally, click the "Perform Sentiment Analysis" button to analyze the sentiment of the entered text.

## Dependencies
- NLTK: Natural Language Toolkit for natural language processing.
- Streamlit: Open-source Python library for creating web applications.
- BART: Bidirectional and Auto-Regressive Transformers, a transformer-based model developed by Facebook AI. It is designed for various natural language processing tasks, including text generation and summarization.

## Limitations
- Sentiment analysis function performs poorly when dealing with sarcastic text (best used for academic or more formal text).
- Only docx,txt and pdf files can be uploaded for now
