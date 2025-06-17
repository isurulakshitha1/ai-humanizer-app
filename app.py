import streamlit as st

st.title("AI Humanizer: Humanize Your Text or Markdown")

# File uploader for Markdown or text files
uploaded_file = st.file_uploader("Upload a Markdown (.md) or text file", type=["md", "txt"])

# Text area for direct input
input_text = st.text_area("Or paste your text here:")

content = ""
if uploaded_file is not None:
    # Read uploaded file as string
    content = uploaded_file.read().decode("utf-8")
    st.write("### File Content:")
    st.markdown(content)
elif input_text:
    content = input_text
    st.write("### Input Text:")
    st.markdown(content)
else:
    st.info("Upload a file or paste text above to get started.")

# (Next step: Add AI humanizer logic and download button)
