import streamlit as st
from libretranslatepy import LibreTranslateAPI
import requests
from requests.exceptions import RequestException
import time

# Initialize LibreTranslateAPI with your endpoint URL
lt = LibreTranslateAPI("https://translate.terraprint.co/")

# Streamlit app starts here
def main():
    st.title("Language Translation App")
    
    # Input box for user to enter text
    user_input = st.text_area("Enter a word or sentence:")
    
    # Dropdown for selecting target language
    languages = ['ar', 'fr', 'es', 'de']  # Example languages
    target_language = st.selectbox("Select target language:", languages)
    
    if st.button("Translate"):
        if user_input:
            try:
                # Detect language of input text
                detected_language = lt.detect(user_input)[0]['language']
                
                # Translate to selected target language
                translated_text = lt.translate(user_input, detected_language, target_language)
                
                # Display translated text
                st.success(f"Translated Text: {translated_text}")
                
            except RequestException as e:
                st.error(f"Error: {e}")
                
                # Retry logic with exponential backoff (up to 3 retries)
                retries = 3
                delay = 1
                for attempt in range(retries):
                    try:
                        st.warning(f"Retrying attempt {attempt + 1}...")
                        time.sleep(delay)
                        translated_text = lt.translate(user_input, detected_language, target_language)
                        st.success(f"Translated Text: {translated_text}")
                        break
                    except RequestException as e:
                        st.error(f"Error on attempt {attempt + 1}: {e}")
                        delay *= 2  # Exponential backoff
                    
        else:
            st.warning("Please enter some text to translate.")

if __name__ == "__main__":
    main()
