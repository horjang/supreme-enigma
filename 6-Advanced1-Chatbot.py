# Generate a streamlit app for your chatbot application created in Project 4

# ⚠️ TODO 5: Integrate Chatbot with Streamlit UI (Hard)
#
# TASK: Create a multi-page chatbot app with Home page (video) and Chatbot page (interactive chat)
#
# SUCCESS CRITERIA:
# - Import chatbot functions (load_model, bot_respond) from chatbot.py
# - Import streamlit
# - Create title "My Chatbot App"
# - Create sidebar with "Home" and "Chatbot" page options
# - Home page: Display markdown message + YouTube video
# - Chatbot page: Load model, get user input, display bot response with spinner
# - Use st.spinner to show loading state
#
# HINTS:
# - from chatbot import load_model, bot_respond
# - import streamlit as st
# - st.sidebar.selectbox('Label', ['Option1', 'Option2'])
# - st.markdown('Text content')
# - st.video('https://youtu.be/VIDEO_ID')
# - text = st.text_input('You:')
# - if text: ... (check if not empty)
# - with st.spinner('Loading...'): st.write(bot_respond(text))
#
# Your code here:

# Import load_model, bot_respond from chatbot
from chatbot import load_model, bot_respond
# Import streamlit package
import streamlit as st

# Insert title 'My Chatbot App'
st.title('My Chatbot App')

# Sidebar
# Insert a sidebar title 'Sidebar'
st.sidebar.title('Sidebar')
# Insert a sidebar subheader 'Pages'
st.sidebar.subheader('Pages')
# Insert a sidebar selectbox 'Select a page' with options 'Home' and 'Chatbot' and assign it to variable 'app_mode'
st.sidebar.selectbox('Select a page', ['Home', 'Chatbot'])

# If app_mode is 'Home'
if app_mode == 'Home':
    # Display 'Chat with me if you feel bored' using st.markdown
    st.markdown('Chat with me if u feel bored')
    # Display any video from youtube using st.video
    st.video()
# Else if app_mode is 'Chatbot'
else:
    # Display 'Please talk to me' using st.text
    st.text('Please talk to me')
    # Call load_model
    if "model_loaded" not in st.session_state:
        load_model()
        st.session_state.model_loaded = True
    # Insert a text input 'You:' and assign it to variable 'text'
    text = st.text_input('You:')
    # If text is not empty
    if text:
        # Display 'Chatbot:' using st.write
        st.write('Chatbot:')
        # While the response is loading, display 'Loading...' using st.spinner
        with st.spinner('Loading...'):
            # Display the response from bot_respond(text) using st.write
            st.write(bot_respond(text))

# Run the app:
# py -m streamlit run 6-Advanced1-Chatbot.py
