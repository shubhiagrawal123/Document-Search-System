import streamlit as st

st.set_page_config(
    page_title="Document Search & Extraction System",
    page_icon="📚",
    layout="wide"
)

# Hero Section
st.markdown("""
<div style='text-align:center;padding:30px'>
    <h1 style='color:#F37021;'>
        📚 Intelligent Document Search & Extraction System
    </h1>
    <h3 style='color:#002D62;'>
        Search, Analyze and Manage Documents Efficiently
    </h3>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Project Description

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("""
    ## 📖 About the Project

    The Intelligent Document Search & Extraction System is designed to
    automatically extract text from multiple document formats and make
    information retrieval easier.

    The system supports:

    - PDF Documents
    - Word Documents (.docx)
    - PowerPoint Presentations (.pptx)
    - Excel Files (.xlsx)
    - CSV Files
    - JSON Files
    - Text Files

    Users can quickly search and analyze large collections of documents
    without manually opening every file.
    """)

with col2:

    st.info("""
    🎯 Objective

    To provide a centralized platform
    for document indexing, searching,
    and analytics.
    """)

st.markdown("---")

# Features

st.subheader("🚀 Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
    📄 Multi-Format Support

    Read and process PDF,
    DOCX, PPTX, XLSX,
    CSV, TXT and JSON files.
    """)

with col2:
    st.success("""
    🔍 Fast Search Engine

    Quickly locate information
    from large document
    collections.
    """)

with col3:
    st.success("""
    📊 Analytics Dashboard

    Visualize document
    distribution and
    file statistics.
    """)

st.markdown("---")

# Workflow

st.subheader("⚙️ System Workflow")

st.markdown("""
1. Upload or place files inside the data folder.
2. Documents are automatically indexed.
3. Text is extracted from supported file formats.
4. Search and analytics modules process the indexed data.
5. Results are displayed through an interactive dashboard.
""")

st.markdown("---")

# Technology Stack

st.subheader("🛠 Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.metric("Frontend", "Streamlit")
tech2.metric("Backend", "Python")
tech3.metric("Visualization", "Plotly")
tech4.metric("Document Parsing", "PyPDF2 / DOCX / PPTX")

st.markdown("---")

st.success(
    "✅ Navigate using the sidebar to access Dashboard, Search Documents, and Analytics."
)