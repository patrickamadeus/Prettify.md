import os, tempfile
from io import StringIO
import logging
import streamlit as st

from chains.base import PrettifyChain


# -- App Header --
st.title('Prettify.md 🎨')
st.markdown("**Refine** words. **Empower** content.")


# -- States --
st.session_state.file = None
st.session_state.before = None
st.session_state.after = None
file_uploader = st.file_uploader(
    label="Upload a Markdown file", 
    type=["md"], 
    label_visibility="collapsed",
    # on_change=on_change_file_uploader,
)


# -- Layouts & Grids --
verbose = st.empty()
spinner = st.spinner("Prettifying...")
button = st.button(
    label="Prettify!", 
)
before_container, after_container = st.columns(2, gap="large")

before_container.header("Original")
before_md = before_container.empty()

after_container.header("Prettified!")
after_md = after_container.empty()


if file_uploader is not None:
    # To convert to a string based IO:
    stringio = StringIO(file_uploader.getvalue().decode("utf-8"))

    # To read file as string:
    string_data = stringio.read()
    st.session_state.before = string_data
    before_md.markdown(string_data)

prettify = PrettifyChain()

if button:
    if st.session_state.before is not None:
        try:
            with spinner:
                result = prettify.run(
                    text = st.session_state.before,
                    input_path=None,
                    output_path=None,
                    verbose_cost=True,
                )
            st.session_state.after = result
            after_md.markdown(result.strip("```"))
            verbose.success("Success!")
        except Exception:
            verbose.error("Something went wrong!")
    else:
        verbose.warning("Please upload a Markdown file")
        before_md.empty()
