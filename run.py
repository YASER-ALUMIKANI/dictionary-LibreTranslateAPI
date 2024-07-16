'''
from libretranslatepy import LibreTranslateAPI
lt = LibreTranslateAPI("https://translate.terraprint.co/")
s = input('enter word or sentence \n')
detec = lt.detect(s)[0]['language']

print(lt.translate(s, detec, "ar"))
'''

import streamlit as st
from libretranslatepy import LibreTranslateAPI

# Initialize LibreTranslateAPI with your endpoint URL
lt = LibreTranslateAPI("https://translate.terraprint.co/")

# List of languages supported by LibreTranslate (you can customize this list)
supported_languages = {
    'English': 'en',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Arabic': 'ar'
}


# Streamlit app starts here
def main():
    st.title("Language Translation App")

    # Input box for user to enter text
    user_input = st.text_area("Enter a word or sentence:")

    # Dropdown menu for selecting the target language
    target_language = st.selectbox("Select Target Language:", list(supported_languages.keys()))

    if st.button("Translate"):
        if user_input:
            # Detect language of input text
            detected_language = lt.detect(user_input)[0]['language']

            # Get language code for selected target language
            target_language_code = supported_languages.get(target_language)

            # Translate to selected language
            translated_text = lt.translate(user_input, detected_language, target_language_code)

            # Display translated text
            st.success(f"Translated Text ({target_language}): {translated_text}")
        else:
            st.warning("Please enter some text to translate.")


if __name__ == "__main__":
    main()
