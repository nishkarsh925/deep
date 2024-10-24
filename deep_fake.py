import streamlit as st
import requests
import base64
import uuid

# Function to detect deepfake
def detect_deepfake(doc_base64, req_id, doc_type):
    url = "https://ping.arya.ai/api/v1/deepfake-detection/image"
    headers = {
        "token": "9872facbf46a6a9ca92fe6e54c82a81e",  
        "content-type": "application/json"
    }
    payload = {
        "doc_base64": doc_base64,
        "req_id": req_id,
        "isIOS": False,
        "doc_type": doc_type,
        "orientation": 0  # Adjust as needed
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# Streamlit app layout
st.title("Deepfake Detection Tool")
uploaded_file = st.file_uploader("Choose an image or video file", type=["jpg", "png", "mp4"])

if uploaded_file is not None:
    # Convert the file to a base64 string
    file_bytes = uploaded_file.read()
    doc_base64 = base64.b64encode(file_bytes).decode('utf-8')
    req_id = str(uuid.uuid4())  # Generate a unique request ID
    doc_type = "image" if uploaded_file.type.startswith('image/') else "video"

    if st.button("Detect Deepfake"):
        result = detect_deepfake(doc_base64, req_id, doc_type)
        st.write("Detection Result:")
        st.write(result)
else:
    st.error("Please upload a file first.")
