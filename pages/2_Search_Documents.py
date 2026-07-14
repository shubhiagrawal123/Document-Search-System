import os

import streamlit as st

from utils.search_engine import (
    load_documents,
    search_keyword
)

DATA_FOLDER = "data_files"

st.title(
    "🔍 Search Documents"
)

if "search_history" not in st.session_state:

    st.session_state.search_history = []

query = st.text_input(
    "Enter Keyword"
)

if query:

    documents = load_documents(
        DATA_FOLDER
    )

    results = search_keyword(
        query,
        documents
    )

    st.session_state.search_history.append(
        query
    )

    st.success(
        f"{len(results)} matching file(s) found."
    )

    if len(results) == 0:

        st.error(
            "No match found."
        )

    for i, result in enumerate(results):

        st.markdown("---")

        st.subheader(
            f"📄 {result['file']}"
        )

        text = result["text"]

        position = text.lower().find(
            query.lower()
        )

        start = max(
            position - 100,
            0
        )

        end = min(
            position + 300,
            len(text)
        )

        preview = text[start:end]

        with st.expander(
            "View Preview"
        ):

            st.text(
                preview
            )

        st.code(
            result["path"]
        )

        if st.button(
            f"Open File {i}"
        ):

            try:

                os.startfile(
                    result["path"]
                )

            except Exception as e:

                st.error(
                    str(e)
                )

st.sidebar.title(
    "Recent Searches"
)

for item in reversed(
    st.session_state.search_history[-10:]
):

    st.sidebar.write(
        item
    )