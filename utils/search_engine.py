import os
import streamlit as st

from utils.file_reader import (
    read_pdf,
    read_txt,
    read_docx,
    read_csv,
    read_xlsx,
    read_pptx,
    read_json
)


@st.cache_data
def load_documents(data_folder):

    documents = []

    if not os.path.exists(data_folder):
        return documents

    for file_name in os.listdir(data_folder):

        file_path = os.path.join(
            data_folder,
            file_name
        )

        if not os.path.isfile(file_path):
            continue

        extension = file_name.split(".")[-1].lower()

        text = ""

        try:

            if extension == "pdf":
                text = read_pdf(file_path)

            elif extension in [
                "txt",
                "py",
                "html",
                "md"
            ]:
                text = read_txt(file_path)

            elif extension == "docx":
                text = read_docx(file_path)

            elif extension == "csv":
                text = read_csv(file_path)

            elif extension == "xlsx":
                text = read_xlsx(file_path)

            elif extension == "pptx":
                text = read_pptx(file_path)

            elif extension == "json":
                text = read_json(file_path)

            else:
                continue

            documents.append({

                "file": file_name,
                "path": os.path.abspath(file_path),
                "extension": extension,
                "text": text

            })

        except Exception as e:

            print(
                f"Error reading {file_name}: {e}"
            )

    return documents


def search_keyword(
    keyword,
    documents
):

    results = []

    keyword = keyword.lower()

    for doc in documents:

        if keyword in doc["text"].lower():

            results.append(doc)

    return results