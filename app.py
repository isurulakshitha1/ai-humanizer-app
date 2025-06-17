import streamlit as st

def simple_humanizer(text):
    # Placeholder: reverse the text (replace with real AI logic later)
    return text[::-1]

st.title("AI Humanizer: Humanize Your Text or Markdown")

uploaded_file = st.file_uploader("Upload a Markdown (.md) or text file", type=["md", "txt"])
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

# Humanize button and output
if content:
    if st.button("Humanize Content"):
        humanized = simple_humanizer(content)
        st.write("### Humanized Output:")
        st.markdown(humanized)
        
