import streamlit as st

# Placeholder humanizer function (replace with real AI logic later)
def simple_humanizer(text):
    # For demonstration, just reverse the text (replace with your AI model)
    return text[::-1]

st.title("AI Humanizer: Humanize Your Text or Markdown")

st.write(
    """
    Upload a Markdown (.md) or text (.txt) file, or paste your text below.
    Click "Humanize Content" to rewrite your content in a more human-like style.
    You can then download the humanized result as a Markdown file.
    """
)

# File uploader for Markdown or text files
uploaded_file = st.file_uploader(
    "Upload a Markdown (.md) or text file", type=["md", "txt"]
)

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

# Humanize button and output
if content:
    if st.button("Humanize Content"):
        humanized = simple_humanizer(content)
        st.write("### Humanized Output:")
        st.markdown(humanized)

        # Download button for the humanized text
        st.download_button(
            label="Download Humanized Text",
            data=humanized,
            file_name="humanized_output.md",
            mime="text/markdown"
        )
        
