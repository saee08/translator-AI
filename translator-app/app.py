import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import pyttsx3
from PIL import Image

# Initialize translator and text-to-speech engine
translator = Translator()
engine = pyttsx3.init()

# Set page configuration for better display
st.set_page_config(page_title="AI Translator & Speech", layout="wide")

# Load a logo or background image (optional)
try:
    image = Image.open("C:/Users/saee santosh pawar/OneDrive/Desktop/th.jpeg")  # Replace with your logo image path
    st.image(image, width=150)
except:
    st.markdown("<h1 style='text-align: center;'> AI Multi-Language Translator & Speech</h1>", unsafe_allow_html=True)

# Introduction section
st.markdown("""
    <p style="text-align: center; font-size: 20px;"> 🌍 Welcome to the AI-powered Translator & Speech App!<br>
    Translate text to different languages and hear it in speech with the power of AI. 🎧</p>
    """, unsafe_allow_html=True)

# User input text area
text = st.text_area("Enter text to translate:", placeholder="Type your text here...", height=150)

# Language selection
language_options = list(LANGUAGES.values())

source_lang = st.selectbox("Select source language (auto-detect by default):", ["Auto Detect"] + language_options)
target_lang = st.selectbox("Select target language:", language_options)

# Map the language names to their language codes
source_lang_code = 'auto' if source_lang == "Auto Detect" else [code for code, name in LANGUAGES.items() if name == source_lang][0]
target_lang_code = [code for code, name in LANGUAGES.items() if name == target_lang][0]

# Output options: Translate text or Translate + Speak
st.subheader("Choose Output Type")

# Two options: Text Translation and Translate + Speech
output_option = st.radio("Select output type:", 
                         ["Translate Text🌍", "Translate Text with 🎧 Speak"])

# Button to perform translation and speech
if st.button("Translate"):
    if text:
        try:
            # Translate the text
            with st.spinner('Translating...'):
                translated_text = translator.translate(text, src=source_lang_code, dest=target_lang_code)
                
                # Display the translated text
                st.success(f"**Translated Text:** {translated_text.text}")

                if output_option == "Translate Text with 🎧 Speak":
                    # Text-to-Speech conversion using gTTS for translated text
                    speed = st.slider("Speech Speed", 0.5, 1.5, 1.0)
                    speech = gTTS(text=translated_text.text, lang=target_lang_code, slow=False)
                    speech.save("translated_speech.mp3")
                    st.audio("translated_speech.mp3", format='audio/mp3')

                    # Option to use pyttsx3 engine for speaking (non-web-based text-to-speech)
                    engine.say(translated_text.text)
                    engine.runAndWait()  # This will make the app speak the translated text using pyttsx3

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("⚠️ Please enter some text to translate!")

# Add a footer
st.markdown("""
    <footer style="text-align: center; font-size: 12px; color: #888;">
    <p>Powered by AI & Streamlit | Developed by Saee Santosh Pawar</p>
    </footer>
    """, unsafe_allow_html=True)

# Display Translated Text in a styled box
if 'translated_text' in locals():
    st.markdown(f"""
    <div style="border: 2px solid #d1f7e0; padding: 20px; border-radius: 10px;">
        <h3>Translated Text</h3>
        <p>{translated_text.text}</p>
    </div>
    """, unsafe_allow_html=True)


# Adding a refresh button for a cleaner experience (optional)
if st.button("Refresh App"):
    st.script_run_ctx().rerun() 