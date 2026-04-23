import streamlit as st
import fasttext
import re
import requests
import os

# -------------------------------
# Load model from Google Drive
# -------------------------------
@st.cache_resource
def load_model():
    model_path = "model.ftz"

    if not os.path.exists(model_path):
        url = "https://drive.google.com/uc?id=1DxxTJ13UeYAH9fD3kAltqzPVQKKLPjNF"
        
        with st.spinner("Downloading model... please wait"):
            r = requests.get(url)
            with open(model_path, "wb") as f:
                f.write(r.content)

    return fasttext.load_model(model_path)

model = load_model()

# -------------------------------
# Text cleaning
# -------------------------------
def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# -------------------------------
# Positive override
# -------------------------------
positive_words = ["happy", "relaxed", "good", "fine", "great", "enjoy", "awesome"]

def is_positive(text):
    return any(word in text for word in positive_words)

# -------------------------------
# UI
# -------------------------------
st.set_page_config(page_title="Mental Health Classifier", layout="centered")

st.title("🧠 Mental Health Text Classifier")
st.markdown("Enter text to classify emotional state")

user_input = st.text_area(
    "Enter your text",
    placeholder="Example: I feel anxious and restless lately..."
)

st.markdown("### Try examples:")
st.write("- I feel very anxious and worried")
st.write("- I have lost interest in everything")
st.write("- I feel happy and relaxed today")
st.write("- I want to end my life")

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):

    if user_input.strip() == "":
        st.error("Please enter some text.")
    else:
        cleaned = clean_text(user_input)

        labels, probs = model.predict([cleaned])
        raw_label = labels[0][0].replace("__label__", "")
        confidence = float(probs[0][0])

        LOW = 0.5
        HIGH = 0.75

        final_label = raw_label
        status = "High confidence"
        warning_msg = None

        # Positive override
        if is_positive(cleaned) and raw_label != "Normal":
            if confidence < 0.9:
                final_label = "Normal"
                status = "Adjusted (positive tone)"
                warning_msg = "Adjusted to Normal based on positive words."

        # Confidence levels
        else:
            if confidence < LOW:
                status = "Low confidence"
                warning_msg = "⚠️ Model prediction may not be reliable."
            elif confidence < HIGH:
                status = "Moderate confidence"
                warning_msg = "⚠️ Prediction may be uncertain."

        # -------------------------------
        # Display
        # -------------------------------
        st.markdown("---")

        st.subheader("Prediction")
        st.success(final_label)

        st.subheader("Confidence")
        st.write(f"{confidence:.2f}  |  {status}")

        if warning_msg:
            st.warning(warning_msg)

        # Critical safety
        if final_label == "Suicidal":
            st.error("⚠️ This may indicate distress. Please seek professional help.")

# -------------------------------
# Disclaimer
# -------------------------------
st.markdown("---")
st.info("This AI model is for educational purposes only. It is not a medical diagnosis tool.")