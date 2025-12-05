import streamlit as st
from pathlib import Path

from languageModelAlpha.sentGenerator import genSentence

st.sidebar.title("Language Model Settings")

TEXT_DIR = Path('languageModelAlpha')
candidates = sorted(p.name for p in TEXT_DIR.glob("*.txt"))

if not candidates:
    st.sidebar.error("No .txt files found in languageModelAlpha")
    st.stop()

corpus_file = st.sidebar.selectbox("Corpus file", candidates)
max_words = st.sidebar.slider("Max words per sentence", 5, 50, 20)
num_sentences = st.sidebar.slider("Number of sentences", 1, 10 ,3)
seed = st.sidebar.number_input("Random seed (optional)", value=42, step=1)

st.title("Language Model Alpha - Web Demo")

st.markdown(
    """
This app uses your **LanguageModelAlpha** package.

1. Pick a corpus file in the sidebar
2. Choose how many words/sentences
3. Click **Generate**
"""
)

with st.expander("Preview Corpus file"):
    txt_path = TEXT_DIR/corpus_file
    preview = txt_path.read_text(encoding="utf-8").splitlines()[:15]
    st.code("\n".join(preview), language="text")

if st.button("Generate"):
    if seed:
        import random
        random.seed(int(seed))
    
    st.subheader("Generated text")
    for i in range(num_sentences):
        sentence = genSentence()
        st.write(f'{i+1}. {sentence}')