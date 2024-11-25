from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
documents=SimpleDirectoryReader("data").load_data()

index=VectorStoreIndex.from_documents(documents,show_progress=True)