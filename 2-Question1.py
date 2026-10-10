# claude-template-fix: leaks-v1
import numpy as np
import pandas as pd

# ⚠️ TODO 1: Import and Display Basic Streamlit Elements (Easy)
#
# TASK: Import streamlit and create basic text elements (title, header, text, markdown)
#
# SUCCESS CRITERIA:
# - Import streamlit as st
# - Create title "My First Streamlit App"
# - Create header "Details of my first Streamlit App"
# - Display text "This is my first streamlit app"
# - Display markdown with blue text
#
# HINTS:
# - import streamlit as st
# - st.title('Your Title Here')
# - st.header('Your Header Here')
# - st.text('Your text here')
# - st.markdown('<p style="color:blue">Text</p>', unsafe_allow_html=True)
#
# Your code here:
import streamlit as st

# Insert a streamlit title 'My First Streamlit App'
st.title('My First Streamlit App')


# Insert a streamlit header 'Details of my first Streamlit App'
st.header('Details of my first Streamlit App')

# Insert streamlit text 'This is my first streamlit app'
st.text('This is my first streamlit app')

# Insert streamlit markdown '<p style="color:blue">A very cool app</p>'
# In the function, set the parameter "unsafe_allow_html" to True
st.markdown('<p style="color:blue">A very cool app</p>', unsafe_allow_html=True)

# Run the app:
# py -m streamlit run 2-Question1.py
