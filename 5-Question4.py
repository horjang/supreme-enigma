# Create an app with 2 pages: Home and About me

# ⚠️ TODO 4: Create Multi-Page App with Sidebar (Medium)
#
# TASK: Build app with sidebar navigation to switch between Home and About me pages
#
# SUCCESS CRITERIA:
# - Import streamlit
# - Create title "My App with 2 Pages"
# - Create sidebar with title "Sidebar"
# - Create selectbox with page options "Home" and "About me"
# - Display different content based on selected page
# - Home page: header + text
# - About me page: header + text
#
# HINTS:
# - import streamlit as st
# - st.title('Title')
# - st.sidebar.title('Sidebar Title')
# - page = st.sidebar.selectbox('Label', ('Option1', 'Option2'))
# - Use if/else to check: if page == 'Home': ...
# - st.header('Header text')
# - st.write('Text content')
#
# Your code here:

# Import streamlit package
import streamlit as st

# Insert title 'My App with 2 Pages'
st.title('My App with 2 Pages')

# Insert a sidebar with 2 options: Home and About me
# Insert a sidebar title 'Sidebar'
st.sidebar.title('Home and About Me')

# Insert a sidebar selectbox 'Select page' with options 'Home' and 'About me' and assign it to variable 'page'
page = st.sidebar.selectbox('Select page', ('Home', 'About'))

# If page is 'Home'
if page == 'Home':
    # Insert a header 'Home'
    st.header('Home')
    # Insert text 'This is my home page' using st.write
    st.write('This is my home page')
# Else
else:
    # Insert a header 'About me'
    st.header('About me')
    # Insert text 'This is my about me page' using st.write
    st.write('This is my about me page')

# Run the app:
# py -m streamlit run 5-Question4.py
