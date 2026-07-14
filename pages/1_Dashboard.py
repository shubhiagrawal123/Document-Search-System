import pandas as pd
import streamlit as st

from utils.search_engine import (
    load_documents
)

DATA_FOLDER = "data_files"

st.title("📊 Dashboard")

documents = load_documents(
    DATA_FOLDER
)

total_files = len(
    documents
)

file_types = {}

for doc in documents:

    ext = doc["extension"].upper()

    file_types[ext] = file_types.get(
        ext,
        0
    ) + 1

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Files",
        total_files
    )

with col2:
    st.metric(
        "File Types",
        len(file_types)
    )

with col3:
    st.metric(
        "Search Mode",
        "Keyword"
    )

st.markdown("---")

st.subheader(
    "Files By Type"
)

if file_types:

    df = pd.DataFrame({

        "Type": list(
            file_types.keys()
        ),

        "Count": list(
            file_types.values()
        )

    })

    st.bar_chart(
        df.set_index("Type")
    )

st.markdown("---")

st.subheader(
    "Indexed Files"
)

table_data = []

for doc in documents:

    table_data.append({

        "File Name": doc["file"],
        "Type": doc["extension"].upper()

    })

if table_data:

    st.dataframe(
        pd.DataFrame(table_data),
        use_container_width=True
    )