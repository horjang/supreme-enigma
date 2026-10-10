# Create a form that allows users to enter their personal details and submit it.

# Import streamlit package
import streamlit as st

# Insert title 'My Personal Details Form'
st.title('My Personal Details Form')
# Insert subheader 'Please enter your personal details'
st.subheader('Please enter your personal details')

# ⚠️ TODO 3: Create Form Input Fields (Medium)
#
# TASK: Add various input fields (text, number, textarea, selectbox, camera, checkbox) and submit button
#
# SUCCESS CRITERIA:
# - Create text input for Name
# - Create number input for Age
# - Create text area for Address
# - Create selectbox for Gender with options 'Male' and 'Female'
# - Create camera input for Photo
# - Create checkbox for agreement
# - Create submit button
# - Display personalized message when submitted
#
# HINTS:
# - name = st.text_input('Label')
# - age = st.number_input('Label')
# - address = st.text_area('Label')
# - gender = st.selectbox('Label', ('Option1', 'Option2'))
# - photo = st.camera_input('Label')
# - agree = st.checkbox('Label text')
# - submit = st.button('Button text')
# - Use string concatenation: 'Text ' + variable + ' more text'
# - Convert number to string: str(age)
#
# Your code here:

# Insert a text input field for 'Name' and assign it to a variable 'name'
name = st.text_input('Name')
# Insert a number input field for 'Age' and assign it to a variable 'age'

# Insert a text area field for 'Address' and assign it to variable 'address'
address = st.text_area('Address')
# Insert a selectbox for 'Gender' with options 'Male' and 'Female' and assign it to 'gender'
gender = st.selectbox('Gender', ('Male', 'Female'))

# Insert a camera input field for 'Photo' and assign it to variable 'photo'
photo = st.camera_input('Photo')

# Insert a checkbox for 'I agree to the terms and conditions' and assign it to variable 'agree'
agree = st.checkbox('I agree to the terms and conditions')
# Insert a button for 'Submit' and assign it to variable 'submit'
submit = st.button('Submit')
# If submit is clicked
if submit:
    # Display 'Thank you for submitting your details' on the app using st.write
    # Include name, age, address, and gender in the message
    st.write(f"Thank you, {name}! Your details have been submitted.")


# Run the app:
# py -m streamlit run 4-Question3.py
