import streamlit as st
import google.generativeai as genai

# Get Gemini API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

def gemini_humanizer(text):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = (
        "Rewrite the following article to sound natural, engaging, and human, suitable for a blog. "
        "Preserve formatting and Markdown where possible. Here is the article:\n\n"
        + text
    )
    response = model.generate_content(prompt)
    return response.text.strip()

st.title("AI Humanizer: Humanize Your Text or Markdown")

st.write(
    """
    Upload a Markdown (.md) or text (.txt) file, or paste your text below.
    Click "Humanize Content" to rewrite your content in a more human-like style using Gemini AI.
    You can then download the humanized result as a Markdown file.
    """
)

uploaded_file = st.file_uploader(
    "Upload a Markdown (.md) or text file", type=["md", "txt"]
)
input_text = st.text_area("Or paste your text here:")

content = ""
if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.write("### File Content:")
    st.markdown(content)
elif input_text:
    content = input_text
    st.write("### Input Text:")
    st.markdown(content)
else:
    st.info("Upload a file or paste text above to get started.")

if content:
    if st.button("Humanize Content"):
        with st.spinner("Gemini is rewriting your content..."):
            humanized = gemini_humanizer(content)
        st.write("### Humanized Output:")
        st.markdown(humanized)
        st.download_button(
            label="Download Humanized Text",
            data=humanized,
            file_name="humanized_output.md",
            mime="text/markdown"
        )
        
