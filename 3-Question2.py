# claude-template-fix: leaks-v1
# Building a simple streamlit app that:
# 1. Prints 'Goodbye' by default
# 2. Prints 'Hello' if the user clicks on the button 'Say Hello'

import numpy as np
import pandas as pd

# ⚠️ TODO 2: Create Interactive Button App (Medium)
#
# TASK: Build an app with a button that changes displayed text based on user interaction
#
# SUCCESS CRITERIA:
# - Import streamlit
# - Create title "My Greeting Streamlit App"
# - Create button labeled "Say Hello" and store result in variable
# - Display "Hello" if button is clicked, "Goodbye" otherwise
#
# HINTS:
# - import streamlit as st
# - st.title('Title Text')
# - btn = st.button('Button Label')
# - Use if/else: if btn: ... else: ...
# - st.text('Text to display')
#
# Your code here:
import streamlit as st


# Insert a streamlit title 'My Greeting Streamlit App'
st.title('My Greeting Streamlit App')

# Insert streamlit button 'Say Hello' and assign it to a variable 'btn'
btn = st.button('Say Hello')
# If btn is clicked
if btn:
    # Display 'Hello' on the app using st.text
    st.text('Hello')
else:
    # Display 'Goodbye' on the app using st.text
    st.text('Goodbye')


# Run the app:
# py -m streamlit run 3-Question2.py
